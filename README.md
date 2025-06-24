
# 🧾 Feature Description

Below is a list of the 40 features used by the DDoS Detection API, along with their descriptions:

| Feature Name             | Description |
|--------------------------|-------------|
| Dst_Port              | Destination port number (e.g., 80 for HTTP). |
| Protocol              | Protocol used (e.g., 6 for TCP, 17 for UDP). |
| Flow_Duration         | Duration of the flow in microseconds. |
| Tot_Fwd_Pkts          | Total number of packets sent in the forward direction. |
| Tot_Bwd_Pkts          | Total number of packets sent in the backward direction. |
| TotLen_Fwd_Pkts       | Total length (in bytes) of forward packets. |
| Fwd_Pkt_Len_Max       | Maximum packet length in the forward direction. |
| Fwd_Pkt_Len_Mean      | Mean packet length in the forward direction. |
| Fwd_Pkt_Len_Std       | Standard deviation of packet lengths in the forward direction. |
| Bwd_Pkt_Len_Max       | Maximum packet length in the backward direction. |
| Bwd_Pkt_Len_Std       | Standard deviation of packet lengths in the backward direction. |
| Flow_Byts_s           | Number of bytes transferred per second in the flow. |
| Flow_Pkts_s           | Number of packets transferred per second in the flow. |
| Flow_IAT_Mean         | Mean time between two packets (Inter Arrival Time). |
| Flow_IAT_Std          | Standard deviation of inter arrival time. |
| Flow_IAT_Max          | Maximum time between two packets. |
| Flow_IAT_Min          | Minimum time between two packets. |
| Fwd_IAT_Tot           | Total inter arrival time for forward packets. |
| Fwd_IAT_Mean          | Mean inter arrival time for forward packets. |
| Fwd_IAT_Std           | Standard deviation of inter arrival time for forward packets. |
| Fwd_IAT_Max           | Maximum inter arrival time for forward packets. |
| Fwd_IAT_Min           | Minimum inter arrival time for forward packets. |
| Bwd_IAT_Std           | Standard deviation of inter arrival time for backward packets. |
| Bwd_IAT_Max           | Maximum inter arrival time for backward packets. |
| Bwd_IAT_Min           | Minimum inter arrival time for backward packets. |
| Fwd_Header_Len        | Total length of forward packet headers. |
| Bwd_Header_Len        | Total length of backward packet headers. |
| Fwd_Pkts_s            | Number of forward packets per second. |
| Pkt_Len_Max           | Maximum length of a packet in the flow. |
| Pkt_Size_Avg          | Average size of packets in the flow. |
| Fwd_Seg_Size_Avg      | Average size of TCP segments in the forward direction. |
| Bwd_Seg_Size_Avg      | Average size of TCP segments in the backward direction. |
| Subflow_Fwd_Pkts      | Number of packets in the forward subflow. |
| Subflow_Fwd_Byts      | Number of bytes in the forward subflow. |
| Subflow_Bwd_Pkts      | Number of packets in the backward subflow. |
| Subflow_Bwd_Byts      | Number of bytes in the backward subflow. |
| Init_Fwd_Win_Byts     | Initial window size in bytes in the forward direction. |
| Init_Bwd_Win_Byts     | Initial window size in bytes in the backward direction. |
| Fwd_Act_Data_Pkts     | Number of forward packets with actual data (not control packets). |
| Fwd_Seg_Size_Min      | Minimum segment size in the forward direction. |
