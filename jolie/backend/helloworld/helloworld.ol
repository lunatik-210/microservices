include "helloworld.iol"

execution { concurrent }

inputPort Server 
{
    Location: "socket://localhost:5000"
    Protocol: http 
    {
        .method = "get";
        .format = "json"
    }
    Interfaces: SumInterface
}

outputPort SumService {
    Location: "socket://localhost:5000"
    Protocol: http
    Interfaces: SumInterface
}

inputPort MainInput {
    Location: "socket://localhost:8000"
    Protocol: http
    {
        .method = "get";
        .format = "json"
    }
    Redirects:
        sum => SumService
    Interfaces: SumInterface
}

main
{
    sum( request )( response ) 
    {
        response.sum = request.x + request.y
    }
}
