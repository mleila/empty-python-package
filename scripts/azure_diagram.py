from diagrams import Diagram
from diagrams.azure.storage import StorageAccounts

with Diagram("Azure Storage Account Diagram", show=False):
    StorageAccounts("Storage Account")