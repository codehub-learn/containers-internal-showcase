from diagrams import Diagram,Edge
from diagrams.aws.compute import EC2
from diagrams.onprem.client import User



with Diagram("EC2", show=False):
    User("User") >> Edge(label="commit") >> EC2("machine")

