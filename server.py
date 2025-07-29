import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/ptwebsolution/api/worldwide-restaurants'

mcp = FastMCP('worldwide-restaurants')

@mcp.tool()
def currencies() -> dict: 
    '''List of Currency'''
    url = 'https://worldwide-restaurants.p.rapidapi.com/currencies'
    headers = {'x-rapidapi-host': 'worldwide-restaurants.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def languages() -> dict: 
    '''List of language'''
    url = 'https://worldwide-restaurants.p.rapidapi.com/languages'
    headers = {'x-rapidapi-host': 'worldwide-restaurants.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def typeahead(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Location Autocomplete'''
    url = 'https://worldwide-restaurants.p.rapidapi.com/typeahead'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'worldwide-restaurants.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def search(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Search Restaurants'''
    url = 'https://worldwide-restaurants.p.rapidapi.com/search'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'worldwide-restaurants.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def detail(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Restaurant Detail'''
    url = 'https://worldwide-restaurants.p.rapidapi.com/detail'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'worldwide-restaurants.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def photos(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Restaurant Photos'''
    url = 'https://worldwide-restaurants.p.rapidapi.com/photos'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'worldwide-restaurants.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def reviews(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Restaurant Reviews'''
    url = 'https://worldwide-restaurants.p.rapidapi.com/reviews'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'worldwide-restaurants.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
