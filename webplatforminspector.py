import requests, re
import json

patterns=[
    (r'/wp-content/plugins/woocommerce/','WooCommerce (Wordpress)'),
    (r'/wp-content/plugins/buddypress/','BuddyPress (Wordpress)'),
    (r'/wp-content/themes/','Wordpress'),
    (r'/euf/assets/','Oracle Service Cloud'),
    (r'cdn.awsli.com.br','Loja Integrada'),
    (r'wixstatic.com','Wix'),
    (r'/static/js/web2py.js','Web2py'),
    (r'/skin/frontend/','Magento'),
    (r'//io\.vtex\.com\.br/','VTex'),
    (r'catalog/view/theme','OpenCart'),
    (r'/_ui/(responsive|addons)/','Hybris'),
    (r'jQuery\.extend\(Drupal\.settings','Drupal'),
    (r'/media/jui/js/','Joomla'),
    (r'\.tray','Tray'),
    (r'cdn\.shopify\.com','Shopify'),
]

def inspect(site):
    tp='Unknown'
    ftp='Unknown'
    if not site.startswith('http'):
        site='http://'+site
    req=requests.get(site)
    html=req.text
    headers=req.headers
    metas=[m.split('>')[0] for m in html.split('<meta')[1:]]
    for meta in metas:
        meta=meta.replace("'",'"')
        if 'name="generator"' in meta:
            ftp=meta.split('content="')[1].split('"')[0]
            tp=ftp.split(' ')[0]
        if 'name="fbits-version"' in meta:
            ftp='TrayCorp by FBITS '+meta.split('content="')[1].split('"')[0]
            tp='TrayCorp'
    if tp=='Unknown':
        for p,t in patterns:
            if re.findall(p,html):
                ftp=t
                tp=t
                break
    return {'platform':tp,'fullname':ftp,'headers':dict(headers)}

if __name__ == '__main__':
    import sys
    site=sys.argv[1]
    print json.dumps(inspect(site),indent=2)

