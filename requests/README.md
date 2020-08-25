## Python Requests

Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, thanks to urllib3.

### 1. Example

```python
import json
import requests

url = "https://www.baidu.com/"
res = requests.get(url)
status_code = res.status_code
try:
    result = res.json()
except json.decoder.JSONDecodeError:
    result = res.content
print(result)
```

### 2. import requests

* 当一个模块首次被导入时，Python 会搜索该模块，如果找到就创建一个module对象并初始化它
* __init__.py in requests
```python
from . import utils
from . import packages
from .models import Request, Response, PreparedRequest
from .api import request, get, head, post, patch, put, delete, options
from .sessions import session, Session
from .status_codes import codes
from .exceptions import (
    RequestException, Timeout, URLRequired,
    TooManyRedirects, HTTPError, ConnectionError,
    FileModeWarning, ConnectTimeout, ReadTimeout
)
```
* dir(requests)
```shell
['ConnectTimeout', 'ConnectionError', 'DependencyWarning', 'FileModeWarning', 'HTTPError', 'NullHandler', 'PreparedRequest', 'ReadTimeout', 'Request', 'RequestException', 'RequestsDependencyWarning', 'Response', 'Session', 'Timeout', 'TooManyRedirects', 'URLRequired', '__author__', '__author_email__', '__build__', '__builtins__', '__cached__', '__cake__', '__copyright__', '__description__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__title__', '__url__', '__version__', '_check_cryptography', '_internal_utils', 'adapters', 'api', 'auth', 'certs', 'chardet', 'check_compatibility', 'codes', 'compat', 'cookies', 'delete', 'exceptions', 'get', 'head', 'hooks', 'logging', 'models', 'options', 'packages', 'patch', 'post', 'put', 'request', 'session', 'sessions', 'ssl', 'status_codes', 'structures', 'urllib3', 'utils', 'warnings']
```

### 3. requests.get

```python
def get(url, params=None, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)
```
### 4. requests.request

```python
def request(method, url, **kwargs):
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)
```
* requests.get or other method just pass-through all args to session.request with Session context

### 5. Session context

#### 5.1 with as context manager

```python
class Session(SessionRedirectMixin):
    def __init__(self):
        ...
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
```
* with sessions.Session() as session: create an Session instance and initialized with __init__ function
* then run __enter__ method 
* after everything done within context body, func __exit__ will be executed

#### 5.2 session instance

* __init__
```python
        ...
        self.adapters = OrderedDict()
        self.mount('http://', HTTPAdapter())
```
* Session instance create an OrderedDict adapter  and mount HTTPAdapter to it
* mount Registers a connection adapter to a prefix

#### 5.3  HTTPAdapter


```python
    def __init__(self, pool_connections=DEFAULT_POOLSIZE,
                 pool_maxsize=DEFAULT_POOLSIZE, max_retries=DEFAULT_RETRIES,
                 pool_block=DEFAULT_POOLBLOCK):
        self.proxy_manager = {}
        self.init_poolmanager(pool_connections, pool_maxsize, block=pool_block)
```
* mount append a HTTPAdapter instance to self.adapters
* __init__ init a poolmanager with 10 pool_connections 
* pool_connections: The number of urllib3 connection pools to cache.
* pool_block: Whether the connection pool should block when no free connections are available..
* init_poolmanager Initializes a urllib3 PoolManager
```python
    self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize,
                                       block=block, strict=True, **pool_kwargs)
```
* now stop,talk about urllib3 later,let's come back to request
```python
def request(method, url, **kwargs):
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)
```

### 6. Session request

* with sessions.Session() as session create a session instance with a urllib3 PoolManager
* call session request method and return it's response

#### 6.1 session request


```python
    def request(self, method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None):
```
* familiar ? just pass-through
* session request body Constructs every thing poolmanager need, prepares request url,parameters,body datas,request options and sends it to get response
* 
```python
    prep = self.prepare_request(req)
    resp = self.send(prep, **send_kwargs)
    return resp
```
#### 6.2 session send

```python
    def send(self, request, **kwargs):
        """Send a given PreparedRequest."""
        # Get the appropriate adapter to use
        adapter = self.get_adapter(url=request.url)
        # Start time (approximately) of the request
        start = preferred_clock()
        # Send the request
        r = adapter.send(request, **kwargs)
        # Total elapsed time of the request (approximately)
        elapsed = preferred_clock() - start
        r.elapsed = timedelta(seconds=elapsed)
        # Response manipulation hooks
        r = dispatch_hook('response', hooks, r, **kwargs)
        return 
```
* first get adapters from here by url
```python
    ...
    self.adapters = OrderedDict()
    self.mount('http://', HTTPAdapter())
```
* call adapter send method with PreparedRequest data
* dispatch_hook build response received by adapter send method and return 
* r.elapsed is time used by adapter.send

### 7. HTTPAdapter

* HTTPAdapter instance init a poolmanager
  
```python
    def __init__(self, pool_connections=DEFAULT_POOLSIZE,
                 pool_maxsize=DEFAULT_POOLSIZE, max_retries=DEFAULT_RETRIES,
                 pool_block=DEFAULT_POOLBLOCK):
        self.proxy_manager = {}
        self.init_poolmanager(pool_connections, pool_maxsize, block=pool_block)
```

#### 7.1 HTTPAdapter send
```python
    def send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None)):
        conn = self.get_connection(request.url, proxies)
        url = self.request_url(request, proxies)
        resp = conn.urlopen(
                method=request.method,
                url=url,
                body=request.body,
                headers=request.headers,
                redirect=False,
                assert_same_host=False,
                preload_content=False,
                decode_content=False,
                retries=self.max_retries,
                timeout=timeout
            )
        return self.build_response(request, resp)

```
* get_connection Returns a urllib3 connection for the given URL 
```python
    conn = self.poolmanager.connection_from_url(url)
```
* request_url Obtain the url to use when making the final request
* conn.urlopen in module urllib3 Get a connection from the pool and perform an HTTP request.
* build response received by conn.urlopen

### 8. Conclusions

* All Request Pipline : ->request.get->request.request->session.request->session.send->HTTPAdapter.send->urllib3.urlopen
* All Response Pipline : ->urllib3.urlopen->HTTPAdapter.build_response
* Read requests description again
```shell
    Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, thanks to urllib3.
```