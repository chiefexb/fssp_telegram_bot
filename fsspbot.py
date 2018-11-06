#import asyncio
import aiohttp
import logging
from aiohttp import web
import json
from lxml import etree
#from os import *
#import sys
f = open('../bot.xml')
cfg = etree.parse(f)
cfg_root = cfg.getroot()
TOKEN = cfg_root.find('tel').text
API_URL = 'https://api.telegram.org/bot%s/sendMessage' % TOKEN
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG, filename='/home/bot.log')

async def search_phisycal(self):
    return 1


async def handler(request):
    data = await request.json()
    logging.info(data)
    headers = {
        'Content-Type': 'application/json'
    }
    logging.info(data)
    message = {
        'chat_id': data['message']['chat']['id'],
        'text': data
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL,
                                data=json.dumps(message),
                                headers=headers) as resp:
            try:
                assert resp.status == 200
            except:
                return web.Response(status=500)
    return web.Response(status=200)

#async def init_app(loop):
app = web.Application( middlewares=[])
app.router.add_post('/webhook', handler)
#    return app

#if __name__ == '__main__':
 #   loop = asyncio.get_event_loop()
 #   try:
#        app = loop.run_until_complete(init_app(loop))
web.run_app(app, host='0.0.0.0', port=8080)
#    except Exception as e:
#        print('Error create server: %r' % e)
#    finally:
#        pass
#    loop.close()
