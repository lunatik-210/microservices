type SumRequest:void 
{
    .x:int
    .y:int
}

type SumResponse:void 
{
    .sum:int
}

interface SumInterface 
{
    RequestResponse: sum(SumRequest)(SumResponse)
}
