from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct

class FaqStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        faq_lambda = _lambda.Function(
            self, "FaqLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="app.handler",
            code=_lambda.Code.from_asset("lambda"),
        )

        api = apigw.LambdaRestApi(
            self, "FaqApi",
            handler=faq_lambda,
            proxy=False
        )

        items = api.root.add_resource("health")
        items.add_method("GET")

        ask = api.root.add_resource("ask")
        ask.add_method("POST")
