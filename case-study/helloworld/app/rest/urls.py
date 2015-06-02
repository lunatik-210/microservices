from . import restv1

from resources import HelloWorldResource

restv1.add_resource(HelloWorldResource, '/helloworld')
