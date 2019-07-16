#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import os
import datetime
import requests
from dotenv import load_dotenv
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

name = "GrafanaSnapshotLibrary"

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = os.getenv("BASE_URL")


def get_annotations(time_from=None, time_to=None, alert_id=None, dashboard_id=None, panel_id=None, tags=[], limit=None):
    api_ep = "{}/api/annotations".format(BASE_URL)
    method = "GET"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(API_TOKEN)
    }

    params = {}
    if time_from:
        params["time_from"] = time_from
    if time_to:
        params["time_to"] = time_to
    if alert_id:
        params["alertId"] = alert_id
    if dashboard_id:
        params["dashboardID"] = dashboard_id
    if panel_id:
        params["panelId"] = panel_id
    if tags:
        params["tags"] = tags
    if limit:
        params["limit"] = limit

    response = requests.request(
        method,
        api_ep,
        params=params,
        headers=headers,
        verify=False)
    return response.json()


def create_annotations(tags=None, time_from=None,
                       time_to=None):
    api_ep = "{}/api/annotations".format(BASE_URL)
    method = "POST"
    headers = {
        "Authorization": "Bearer {}".format(API_TOKEN),
        "Content-Type": "application/json"
    }

    post_json = {
        "time": time_from,
        "timeEnd": time_to,
        "isRegion": bool('false'),
        "tags": [tags],
        "text": "Test"
    }

    response = requests.request(
        method,
        api_ep,
        json=post_json,
        headers=headers,
        verify=False)

    return response.json()


def delete_annotations_by_region_id(region_id=None):

    """
    Delete Annotation By RegionId  (https://grafana.com/docs/http_api/annotations/#delete-annotation-by-regionid)
    DELETE /api/annotations/region/:id
    Deletes the annotation that matches the specified region id. A region is an annotation that covers
    a timerange and has a start and end time. In the Grafana database,
    this is a stored as two annotations connected by a region id.
    :param region_id:
    :return a json:
    """

    api_ep = "{}/api/annotations/region/{}".format(BASE_URL, region_id)
    method = "DELETE"
    headers = {
        "Authorization": "Bearer {}".format(API_TOKEN),
        "Content-Type": "application/json"
    }

    response = requests.request(
        method,
        api_ep,
        headers=headers,
        verify=False)

    return response.json()


def get_dashboard(slug):
    api_ep = "{}/api/dashboards/db/{}".format(BASE_URL, slug)
    method = "GET"
    headers = {
        "Authorization": "Bearer {}".format(API_TOKEN),
        "Content-Type": "application/json"
    }

    response = requests.request(
        method,
        api_ep,
        headers=headers,
        verify=False)

    return response.json()


def search_dashboards(query=None, tag=None, starred=None, tagcloud=None):
    api_ep = "{}/api/search".format(BASE_URL)
    method = "GET"
    headers = {
        "Authorization": "Bearer {}".format(API_TOKEN),
        "Content-Type": "application/json"
    }

    params = {}
    if query:
        params["query"] = query
    if tag:
        params["tag"] = tag
    if starred:
        params["starred"] = starred
    if tagcloud:
        params["tagcloud"] = tagcloud

    response = requests.request(
        method,
        api_ep,
        params=params,
        headers=headers,
        verify=False)

    return response.json()


def create_snapshot(dashboard, name=None, expire=None, external=None, key=None, deleteKey=None, time_from=None,
                    time_to=None):
    api_ep = "{}/api/snapshots".format(BASE_URL)
    method = "POST"
    headers = {
        "Authorization": "Bearer {}".format(API_TOKEN),
        "Content-Type": "application/json"
    }

    dashboard = dashboard["dashboard"] if "dashboard" in dashboard else dashboard

    if time_from:
        dashboard["time"]["from"] = time_str_from_unix_ms(time_from)
    if time_to:
        dashboard["time"]["to"] = time_str_from_unix_ms(time_to)

    post_json = {
        "dashboard": dashboard
    }
    if name:
        post_json["name"] = name
    if expire:
        post_json["expire"] = expire
    if external:
        post_json["external"] = external
    if key:
        post_json["key"] = key
    if deleteKey:
        post_json["deleteKey"] = deleteKey

    response = requests.request(
        method,
        api_ep,
        json=post_json,
        headers=headers,
        verify=False)

    return response.json()


def time_str_from_unix_ms(unix_ms):
    return datetime.datetime.utcfromtimestamp(int(unix_ms / 1000)).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def datetime_string_to_timestamp(date_time_str):
    return int(datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S').strftime("%s"))


def get_dashboard_url(key):
    return "{}/dashboard/snapshot/{}".format(BASE_URL,key)


def main():
    parser = argparse.ArgumentParser(description='Create Snapshot on Grafana with official api (https://grafana.com/docs/http_api/)')

    parser.add_argument('-s',"--start",metavar='start', help='Start date time ex. 1563183710618',type=int,  required=True)
    parser.add_argument('-e',"--end",metavar='end', help='End date time ex. 1563185212275', type=int, required=True)
    parser.add_argument('-t',"--tags",metavar='tags', help='Tag in grafana ex. tag-name,tag-name1',
                        required=True)
    args = parser.parse_args()

    date_time_start = int(args.start)
    date_time_end = int(args.end)
    tags = args.tags

    # create annotations with tags, start , end
    annotation_region_id = create_annotations(tags, date_time_start, date_time_end)['id']
    dashboards_info = search_dashboards(tag=tags)
    dashboards = {}
    for dashboard_info in dashboards_info:
        slug = os.path.basename(dashboard_info["uri"])
        print(slug)
        dashboards[slug] = get_dashboard(slug)

    annotations = get_annotations(tags=[tags], time_from=date_time_start, time_to=date_time_end)

    time_regions = {}
    for regionId in set(map(lambda x: x["regionId"], annotations)):
        time_pair = sorted([a["time"] for a in annotations if a["regionId"] == regionId])
        region_str = "{0[0]}_{0[1]}".format(tuple(map(time_str_from_unix_ms, time_pair)))
        time_regions[region_str] = time_pair

    snapshot_list = []
    for slug, dashboard in dashboards.items():
        for region_str, v in time_regions.items():
            snapshot_name = "{}_{}".format(slug, region_str)
            time_from = v[0]
            time_to = v[1]
            snapshot_list.append(get_dashboard_url(create_snapshot(dashboard, name=snapshot_name, time_from=time_from, time_to=time_to)['key']))

    # Remove annotations
    delete_annotations_by_region_id(annotation_region_id)

    print(snapshot_list)


if __name__ == "__main__":
    main()
