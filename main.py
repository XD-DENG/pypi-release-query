import requests
import json
import pandas as pd
import sys

with open(sys.argv[1], "r") as f:
    packages_to_check = [p.strip().split("==")[0] for p in f.readlines()]
n_packages = len(packages_to_check)

query_result = []
i = 0
for package_name in packages_to_check:

    # REFERENCE: https://wiki.python.org/moin/PyPIJSON
    url = "https://pypi.org/pypi/{}/json".format(package_name)

    response = requests.get(url=url)
    if response.status_code == 200:
        response_content = json.loads(response.content)
        latest_version = response_content['info']['version']
        upload_time = response_content['releases'][latest_version][0]['upload_time']

        query_result.append([package_name, latest_version, upload_time])
    else:
        query_result.append([package_name, None, None])

    i += 1
    if (i % 10) == 0:
        print("{}/{} done".format(i, n_packages))


result = pd.DataFrame(query_result, columns=['Package Name', "Latest Version", "Upload Time"])
result.set_index("Package Name", inplace=True)
result.sort_values('Upload Time', inplace=True, ascending=False)

print(result)

