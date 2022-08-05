import timeit
        
def f1():
    s = set(range(100))

    
def f2():
    l = list(range(100))

    
def f3():
    t = tuple(range(100))


def f4():
    s = str(range(100))

    
def f5():
    s = set()
    for i in range(100):
        s.add(i)

def f6():
    l = []
    for i in range(100):
        l.append(i)
    
def f7():
    s_comp = {i for i in range(100)}

    
def f8():
    l_comp = [i for i in range(100)]
    

if __name__ == "__main__":
    t1 = timeit.Timer("f1()", "from __main__ import f1")
    t2 = timeit.Timer("f2()", "from __main__ import f2")
    t3 = timeit.Timer("f3()", "from __main__ import f3")
    t4 = timeit.Timer("f4()", "from __main__ import f4")
    t5 = timeit.Timer("f5()", "from __main__ import f5")
    t6 = timeit.Timer("f6()", "from __main__ import f6")
    t7 = timeit.Timer("f7()", "from __main__ import f7")
    t8 = timeit.Timer("f8()", "from __main__ import f8")
    print("set               :", t1.timeit(), '[ms]')
    print("list              :", t2.timeit(), '[ms]')
    print("tuple             :", t3.timeit(), '[ms]')
    print("string            :", t4.timeit(), '[ms]')
    print("set_add           :", t5.timeit(), '[ms]')
    print("list_append       :", t6.timeit(), '[ms]')
    print("set_comprehension :", t5.timeit(), '[ms]')
    print("list_comprehension:", t6.timeit(), '[ms]')

#Scale-Up : 단일 서버(하드웨어)의 성능을 증가시켜서 더 많은 요청을 처리하는 방법
#단일 하드웨어의 성능을 높이기 위해 CPU, 메모리, 하드디스트 등을 업그레이드 하거나 추가하는 것

#Scale-Out : 동일한 사양의 새로운 서버를 추가하여 성능을 증가시키는 방법
#서버가 증설됨에 따라 여러대의 서버의 트래픽을 나누어 갖게 되고, 각각의 서버가 이를 처리
    
스케일 업은 별도의 서버를 추가하지 않기 때문에 여러 대의 서버를 관리하면서 발생하는 데이터 정합성 이슈에서 자유로움
한대의 서버로 관리하면 별도의 소프트웨어 라이선스 추가 비용 발생 x
하드웨어를 추가 교체 -> 구현이 어렵지 x
한계는 장비의 제한
업그레이드 비용의 제한
스케일 업으로만 성능을 증가시킨 서버는 한대의 모든 클라이언트의 트래픽을 감당해야하기때문에
심각할 경우 해당 서버가 복구되기 전까지 서비스를 중단해야한다.


스케일 아웃 동일한 사양의 새로운 서버를 추가하여 성능을 증가시키는 방법
하나의 노드에서 장애가 발생하더라도 다른 노드에서 서비스 제공가능 가용성을 높일 수 있음
필요에따라 더 많은 서버를 추가/감소 가능
스케일 업은 확장의 한계 < 스케일 아웃은 확장에 유연
스케일 아웃을 하면 로드 밸런싱을 구현해야함
트래픽 증가에따라 서버 로드율, 부하량, 처리 속도 등을 고려하여 여러 대의 서버가 트래픽을 적절히 분담하여 처리
상대적으로 단일 서버에 작업이 쌓여서 멈춘 병목 현상 해결
스케일 아웃의 단점
서버 증가-> 소프트웨어 라이선스 비용증가
데이터 불일치가 잠재적으로 발생할 수있음
다중 서버에서 로그인시에 데이터 불일치 가능성있음


1. Scale-Up은 서버의 성능을 높이기 위해서 CPU, 메모리, 디스크 등의 하드웨어를 추가하거나 더 좋은 하드웨어로 교체하여 단일 서버 자체의 성능을 높이는 것을 의미합니다.

 

2. Scale-Out은 서버의 성능을 높이기 위해서 동일 성능의 서버를 추가하여 부하를 분산시켜 처리 능력이 향상하는 것을 의미합니다.

 

3. Scale-Up과 Scale-Out은 각각 장점과 단점을 갖고 있지만 이에 따라 적절한 시스템에 사용하면 서버 성능에 있어서 긍정적인 효과를 얻을 수 있습니다.

#Scale-Up: How to increase the performance of a single server (hardware) to handle more requests
#Upgrading or adding CPU, memory, hard disk, etc. to increase the performance of a single piece of hardware

#Scale-Out: How to increase performance by adding new servers with the same specs
# As the server is expanded, the traffic of multiple servers is divided, and each server handles it.
    
Because scale-up does not add a separate server, it is free from data consistency issues that occur while managing multiple servers.
If you manage it as one server, you incur additional cost for a separate software license x
Additional replacement of hardware -> difficult to implement x
limits are the limits of the equipment
Limitations on upgrade costs
Because the server, which increases performance only by scaling up, has to handle the traffic of all one client.
In severe cases, the service must be stopped until the server is restored.


Scale-out How to increase performance by adding new servers with the same specs
Even if one node fails, other nodes can provide services.
More servers can be added/reduced as needed
Scale-up is the limit of expansion < Scale-out is flexible to scale
If you scale out, you need to implement load balancing.
As traffic increases, multiple servers divide and process traffic appropriately considering the server load rate, load, and processing speed.
Resolves bottlenecks that have stalled due to accumulating workloads on a relatively single server
Disadvantages of Scale Out
Server increase -> Software license cost increase
Data inconsistencies can potentially occur
Possible data inconsistency when logging in from multiple servers


1. Scale-Up means to increase the performance of a single server itself by adding or replacing hardware such as CPU, memory, disk, etc., with better hardware to increase the performance of the server.

 

2. Scale-Out means to increase the processing power by adding a server of the same performance to increase the performance of the server and distributing the load.

 

3. Scale-Up and Scale-Out each have their advantages and disadvantages, but if used in the appropriate system, they can have a positive effect on server performance.
