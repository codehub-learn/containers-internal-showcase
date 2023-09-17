from diagrams import Diagram,Edge
from diagrams.c4 import Person,Container,SystemBoundary,Database

graph_attr = {
    "splines": "spline",
}




with Diagram("Components in Series", show=False, direction="LR", graph_attr=graph_attr):
    with SystemBoundary("Components in Series"):
        lb = Person(
            name = "Load Balancer",
            description = "99.999%"
        )
        vm = Container(
            name = "Virtual Machine",
            description = "99.5%"
        )
        app = Container(
            name = "Application",
            description = "99.99%"
        )
        db = Database(
            name = "Database",
            description = "99.9%"
        )
        lb >> vm >> app >> db
    with SystemBoundary("Components in Parallel", color="darkorange"):
        lb = Person(
            name = "Load Balancer",
            description = "99.999%"
        )
        vm1 = Container(
            name = "Virtual Machine",
            description = "99.5%"
        )
        app1 = Container(
            name = "Application",
            description = "99.99%"
        )
        db1 = Database(
            name = "Database",
            description = "99.9%"
        )
        vm2 = Container(
            name = "Virtual Machine",
            description = "99.5%"
        )
        app2 = Container(
            name = "Application",
            description = "99.99%"
        )
        db2 = Database(
            name = "Database",
            description = "99.9%"
        )
        lb >> vm1 >> app1 >> db1
        lb >> vm2 >> app2 >> db2