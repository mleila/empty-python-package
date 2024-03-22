from diagrams import Diagram
from diagrams.azure.storage import StorageAccount

with Diagram("Azure Storage Account Diagram", show=False):
    StorageAccount("Storage Account")