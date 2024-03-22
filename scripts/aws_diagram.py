from diagrams import Diagram, Cluster
from diagrams.aws.network import VPC
from diagrams.aws.compute import EC2

with Diagram("AWS Diagram", show=False):
    with Cluster("VPC"):
        EC2("EC2 Instance")
