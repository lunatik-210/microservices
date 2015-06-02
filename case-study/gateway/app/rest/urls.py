from . import restv1

from resources import TokenResource, RefreshTokenResource, UserResource, UsersResource, HelloWorldResource

restv1.add_resource(TokenResource, '/token')
restv1.add_resource(RefreshTokenResource, '/refresh_token')

restv1.add_resource(UserResource, '/users/<int:id>')
restv1.add_resource(UsersResource, '/users')

restv1.add_resource(HelloWorldResource, '/helloworld')
