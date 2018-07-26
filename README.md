# Web Platform Inspector

This simple Python module tries to detect in which platform a website was made.

## Usage:

```bash
python webplatforminspector.py elcio.com.br
```

Output:

```javascript
{
  "platform": "WordPress", 
  "fullname": "WordPress 4.9.7", 
  "headers": {
    "Content-Length": "17031", 
    "Content-Encoding": "gzip", 
    "Accept-Ranges": "bytes", 
    "Vary": "Accept-Encoding", 
    "Keep-Alive": "timeout=2, max=100", 
    "Server": "Apache", 
    "Last-Modified": "Thu, 26 Jul 2018 14:35:33 GMT", 
    "Connection": "Keep-Alive", 
    "ETag": "\"4287-571e7e866cc85\"", 
    "Date": "Thu, 26 Jul 2018 15:09:30 GMT", 
    "Content-Type": "text/html; charset=UTF-8"
  }
}
```

Supported platforms:

* WooCommerce (Wordpress)
* BuddyPress (Wordpress)
* Wordpress
* Oracle Service Cloud
* Loja Integrada
* Wix
* Web2py
* Magento
* VTex
* OpenCart
* Hybris
* Drupal
* Joomla
* Tray
* Shopify

It will also detect any platform that includes a generator meta tag inside served markup.

