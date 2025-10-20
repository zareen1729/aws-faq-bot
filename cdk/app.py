#!/usr/bin/env python3
import aws_cdk as cdk
from faq_stack import FaqStack

app = cdk.App()
FaqStack(app, "FaqBotStack")
app.synth()
