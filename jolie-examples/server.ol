include "twiceInterface.iol"

execution{ concurrent }

inputPort TwiceService {
    Location: "socket://localhost:8800"
    Protocol: sodep
    Interfaces: TwiceInterface
}

main 
{
    twice( number )( response ) {
        response = number * 2
    }
}

/*

include "console.iol"
include "percentInterface.iol"

inputPort PercService {
    Location: "socket://localhost:2000"
    Protocol: sodep
    Interfaces: PercentInterface
}

main
{
    install( TypeMismatch =>
                println@Console( "TypeMismatch: " + main.TypeMismatch )()
    );

    percent( request )( response ){
        response.percent_value = double( request.part )/request.total
    }
}

*/
