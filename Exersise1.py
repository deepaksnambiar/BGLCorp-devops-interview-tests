import json
from datetime import datetime

target_date = datetime.fromisoformat('2022-04-12T13:00:00')

with open('ec2-describe-instances.json', 'r') as f:
    instances = json.load(f)

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        launch_time = datetime.fromisoformat(instance['LaunchTime'])
        if launch_time < target_date:
            print(instance['InstanceId'])