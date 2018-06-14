#!/usr/bin/env python

import os
import asana
import argparse
import json

client = asana.Client.access_token(os.environ['JUSTIN_MOSCOVITZ_PAT'])

parser = argparse.ArgumentParser(description = 'Snark with a bot')
parser.add_argument('-t', '--task_id', type=str)
parser.add_argument('-c', '--comment_id', type=str)
parser.add_argument('-m', '--message', type=str)
parser.add_argument('-l', '--like', action='store_true')
parser.add_argument('-s', '--show_comments', action='store_true')

args = parser.parse_args()

# Can always list the comments.

# OK, let's validate:
if args.task_id and args.comment_id:
    raise "Can't specify both task and comment id"
if args.task_id:
    if args.show_comments:
        stories = client.stories.find_by_task(args.task_id)
        comments = [c for c in stories if c[u'type'] == 'comment']
        str =json.dumps(comments, sort_keys=True, indent=2, separators=(',', ': ')) 
        print(str)
    if args.message:
        # We want to post a message to the given task
        client.stories.create_on_task(args.task_id, {'text': args.message})
    if args.like:
        # We want to like the task (can be run with message too)
        client.tasks.update(args.task_id, {'liked':True})
elif args.comment_id:
    if args.like:
        path = "/stories/%s" % (args.comment_id)
        client.put(path, {'liked':True})
else:
    raise "Must pass one of task_id or comment_id"

