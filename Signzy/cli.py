import click
import urllib3
from common import read_data_file as rdf
from common import make_http_requests as mhr
from common import write_output as wo
import pandas as pd
import numpy as np

@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.obj['DEBUG'] = debug

@cli.command()
@click.pass_context
@click.option('--input_path', default=r'data\address_book.xlsx', help='Path to the input excel sheet file.')
@click.option('--output_path', default=r'output\address_book.xlsx', help='Path to the output excel sheet file.')
def find_geocodes_from_excel_sheet(ctx, input_path, output_path):
    """Function for finding geocoedes from the address given in the Excel workbook file."""
    ctx = ctx.obj['DEBUG']

    df = rdf.read_excel_file(input_path)
    df['latitude'] = np.nan
    df['longitude'] = np.nan

    for index, row in df.iterrows():
        _api_response = mhr.make_post_request(row['Address'])

        df.loc[index, 'latitude'] = _api_response['results'][0]['geometry']['location']['lat']
        df.loc[index, 'longitude'] =  _api_response['results'][0]['geometry']['location']['lng']
    if ctx:
        click.echo('{}'.format(df))
    wo.write_to_excel(df, output_path)
if __name__ == '__main__':
    cli(obj={})
