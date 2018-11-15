import ns.applications
import ns.core
import ns.mobility
import ns.network
import ns.csma

def main(argv):
print "hello"
'''
    cmd = ns.core.CommandLine()
    cmd.backboneNodes = 10
    cmd.AddValue("backboneNodes","number of backbone nodes")
    cmd.Parse(argv)

    backboneNodes = int(cmd.backboneNodes)
    backbone = ns.network.NodeContainer()
    backbone.Create(backboneNodes)

    mobility = ns.mobility.MobilityHelper()
    mobility.SetPositionAllocator("ns3::GridPositionAllocator",
                                 "MinX", ns.core.DoubleValue (1.0),
                                 "MinY", ns.core.DoubleValue (1.0),
                                 "DeltaX",ns.core.DoubleValue (5.0),
                                 "DeltaY", ns.core.DoubleValue (5.0),
                                 "GridWidth", ns.core.UintegerValue (3),
                                 "LayoutType", ns.core.StringValue ("RowFirst"))
    mobility.SetMobilityModel("ns3::RandomWalk2dMobilityModel",
                             "Mode", ns.core.StringValue ("Time"),
                             "Time", ns.core.StringValue ("1s"),
                             "Speed", ns.core.StringValue ("ns3::ConstantRandomVariable[Constant=1.0]"),
                             "Bounds", ns.mobility.RectangleValue (ns.mobility.Rectangle (0.0, 20.0, 0.0, 20.0)))
    mobility.Install(backbone)
    mobility.AssignStreams(backbone, 0)
    csma = ns.csma.CsmaHelper()
    ascii = ns.network.AsciiTraceHelper();
    mobility.EnableAsciiAll(ascii.CreateFileStream("mobility-trace.mob"));

    ns.core.Simulator.Stop(ns.core.Seconds(20))
    ns.core.Simulator.Run()
    ns.core.Simulator.Destroy()

import sys
main(sys.argv)
'''
