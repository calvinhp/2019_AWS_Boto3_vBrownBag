import json
import time
import subprocess

import click
import jmespath as jp


@click.command()
@click.option('-u', '--user', help='db user', prompt=True, required=True)
@click.option('-p', '--password', help='db password',
              prompt=True, required=True, hide_input=True)
@click.option('-h', '--host', help='Source DB Host', prompt=True, required=True)
@click.option('-m', '--mappings', help='db mappings json file', required=True)
def dumpdbstructure(user, password, host, mappings):
    with open(mappings) as f:
        db_map = json.load(f)
        dbs = jp.search('rules[].["object-locator"][].["schema-name"] | []',
                        db_map)

    dump_cmd = [
        'mysqldump',
        '--no-data',
        '--compact',
        '--routines',
        f'--host={host}',
        f'--user={user}',
        f'--password={password}',
        '--databases', ' '.join(dbs)
    ]

    print("Executing")
    print(" ".join(dump_cmd))

    dumpfilename = time.strftime("%Y%m%d-%H%M%S") + '-' + host + '.sql'

#    with open(dumpfilename, 'w') as f:
#        proc = subprocess.Popen(dump_cmd, stdout=f)


if __name__ == '__main__':
    dumpdbstructure()
