# PySNMP SMI module. Autogenerated from smidump -f python SCTP-MIB
# by libsmi2pysnmp-0.0.9-alpha at Fri Jul  9 17:12:45 2010,
# Python version sys.version_info(major=2, minor=7, micro=0, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InetAddress, InetAddressType, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TruthValue")

# Objects

sctpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 104)).setRevisions(("2004-09-02 00:00",))
if mibBuilder.loadTexts: sctpMIB.setOrganization("IETF SIGTRAN Working Group")
if mibBuilder.loadTexts: sctpMIB.setContactInfo("\nWG EMail: sigtran@ietf.org\n\nWeb Page:\n      http://www.ietf.org/html.charters/sigtran-charter.html\n\nChair:     Lyndon Ong\n           Ciena Corporation\n           0480 Ridgeview Drive\n           Cupertino, CA  95014\n           USA\n           Tel:\n           Email: lyong@ciena.com\n\nEditors:   Maria-Carmen Belinchon\n           R&D Department\n           Ericsson Espana S. A.\n           Via de los Poblados, 13\n           28033 Madrid\n           Spain\n           Tel:   +34 91 339 3535\n           Email: Maria.C.Belinchon@ericsson.com\n\n           Jose-Javier Pastor-Balbas\n           R&D Department\n           Ericsson Espana S. A.\n           Via de los Poblados, 13\n           28033 Madrid\n           Spain\n           Tel:   +34 91 339 1397\n    Email: J.Javier.Pastor@ericsson.com")
if mibBuilder.loadTexts: sctpMIB.setDescription("The MIB module for managing SCTP implementations.\n\nCopyright (C) The Internet Society (2004).  This version of\nthis MIB module is part of RFC 3873; see the RFC itself for\nfull legal notices. ")
sctpObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 104, 1))
sctpStats = MibIdentifier((1, 3, 6, 1, 2, 1, 104, 1, 1))
sctpCurrEstab = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpCurrEstab.setDescription("The number of associations for which the current state is\neither ESTABLISHED, SHUTDOWN-RECEIVED or SHUTDOWN-PENDING.")
sctpActiveEstabs = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpActiveEstabs.setDescription("The number of times that associations have made a direct\ntransition to the ESTABLISHED state from the COOKIE-ECHOED\nstate: COOKIE-ECHOED -> ESTABLISHED. The upper layer initiated\nthe association attempt.")
sctpPassiveEstabs = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpPassiveEstabs.setDescription("The number of times that associations have made a direct\ntransition to the ESTABLISHED state from the CLOSED state:\nCLOSED -> ESTABLISHED. The remote endpoint initiated the\nassociation attempt.")
sctpAborteds = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAborteds.setDescription("The number of times that associations have made a direct\ntransition to the CLOSED state from any state using the\nprimitive 'ABORT': AnyState --Abort--> CLOSED. Ungraceful\ntermination of the association.")
sctpShutdowns = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpShutdowns.setDescription("The number of times that associations have made a direct\ntransition to the CLOSED state from either the SHUTDOWN-SENT\nstate or the SHUTDOWN-ACK-SENT state. Graceful termination of\nthe association.")
sctpOutOfBlues = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpOutOfBlues.setDescription("The number of out of the blue packets received by the host.\nAn out of the blue packet is an SCTP packet correctly formed,\nincluding the proper checksum, but for which the receiver was\nunable to identify an appropriate association.")
sctpChecksumErrors = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpChecksumErrors.setDescription("The number of SCTP packets received with an invalid\nchecksum.")
sctpOutCtrlChunks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpOutCtrlChunks.setDescription("The number of SCTP control chunks sent (retransmissions are\nnot included). Control chunks are those chunks different from\nDATA.")
sctpOutOrderChunks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpOutOrderChunks.setDescription("The number of SCTP ordered data chunks sent (retransmissions\nare not included).")
sctpOutUnorderChunks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpOutUnorderChunks.setDescription("The number of SCTP unordered chunks (data chunks in which the\nU bit is set to 1) sent (retransmissions are not included).")
sctpInCtrlChunks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpInCtrlChunks.setDescription("The number of SCTP control chunks received (no duplicate\nchunks included).")
sctpInOrderChunks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpInOrderChunks.setDescription("The number of SCTP ordered data chunks received (no duplicate\nchunks included).")
sctpInUnorderChunks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpInUnorderChunks.setDescription("The number of SCTP unordered chunks (data chunks in which the\nU bit is set to 1) received (no duplicate chunks included).")
sctpFragUsrMsgs = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpFragUsrMsgs.setDescription("The number of user messages that have to be fragmented\nbecause of the MTU.")
sctpReasmUsrMsgs = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpReasmUsrMsgs.setDescription("The number of user messages reassembled, after conversion\ninto DATA chunks.")
sctpOutSCTPPacks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpOutSCTPPacks.setDescription("The number of SCTP packets sent. Retransmitted DATA chunks\nare included.")
sctpInSCTPPacks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpInSCTPPacks.setDescription("The number of SCTP packets received. Duplicates are\nincluded.")
sctpDiscontinuityTime = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 18), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which\nany one or more of this general statistics counters suffered a\ndiscontinuity.  The relevant counters are the specific\ninstances associated with this interface of any Counter32 or\nCounter64 object contained in the SCTP layer statistics\n(defined below sctpStats branch).  If no such discontinuities\nhave occurred since the last re-initialization of the local\nmanagement subsystem, then this object contains a zero value.")
sctpParams = MibIdentifier((1, 3, 6, 1, 2, 1, 104, 1, 2))
sctpRtoAlgorithm = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("vanj", 2), )).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpRtoAlgorithm.setDescription("The algorithm used to determine the timeout value (T3-rtx)\nused for re-transmitting unacknowledged chunks.")
sctpRtoMin = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 2), Unsigned32().clone(1000)).setMaxAccess("readonly").setUnits("milliseconds")
if mibBuilder.loadTexts: sctpRtoMin.setDescription("The minimum value permitted by a SCTP implementation for the\nretransmission timeout value, measured in milliseconds.  More\nrefined semantics for objects of this type depend upon the\nalgorithm used to determine the retransmission timeout value.\n\nA retransmission time value of zero means immediate\nretransmission.\n\nThe value of this object has to be lower than or equal to\nstcpRtoMax's value.")
sctpRtoMax = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 3), Unsigned32().clone(60000)).setMaxAccess("readonly").setUnits("milliseconds")
if mibBuilder.loadTexts: sctpRtoMax.setDescription("The maximum value permitted by a SCTP implementation for the\nretransmission timeout value, measured in milliseconds.  More\nrefined semantics for objects of this type depend upon the\nalgorithm used to determine the retransmission timeout value.\n\nA retransmission time value of zero means immediate re-\ntransmission.\n\n\n\n\n\nThe value of this object has to be greater than or equal to\nstcpRtoMin's value.")
sctpRtoInitial = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 4), Unsigned32().clone(3000)).setMaxAccess("readonly").setUnits("milliseconds")
if mibBuilder.loadTexts: sctpRtoInitial.setDescription("The initial value for the retransmission timer.\n\nA retransmission time value of zero means immediate re-\ntransmission.")
sctpMaxAssocs = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 2147483647L))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpMaxAssocs.setDescription("The limit on the total number of associations the entity can\nsupport. In entities where the maximum number of associations\nis dynamic, this object should contain the value -1.")
sctpValCookieLife = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 6), Unsigned32().clone(60000)).setMaxAccess("readonly").setUnits("milliseconds")
if mibBuilder.loadTexts: sctpValCookieLife.setDescription("Valid cookie life in the 4-way start-up handshake procedure.")
sctpMaxInitRetr = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 7), Unsigned32().clone(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpMaxInitRetr.setDescription("The maximum number of retransmissions at the start-up phase\n(INIT and COOKIE ECHO chunks). ")
sctpAssocTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 3))
if mibBuilder.loadTexts: sctpAssocTable.setDescription("A table containing SCTP association-specific information.")
sctpAssocEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 3, 1)).setIndexNames((0, "SCTP-MIB", "sctpAssocId"))
if mibBuilder.loadTexts: sctpAssocEntry.setDescription("General common variables and statistics for the whole\nassociation.")
sctpAssocId = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sctpAssocId.setDescription("Association Identification. Value identifying the\nassociation. ")
sctpAssocRemHostName = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemHostName.setDescription("The peer's DNS name. This object needs to have the same\nformat as the encoding in the DNS protocol.  This implies that\nthe domain name can be up to 255 octets long, each octet being\n0<=x<=255 as value with US-ASCII A-Z having a case insensitive\nmatching.\n\nIf no DNS domain name was received from the peer at init time\n(embedded in the INIT or INIT-ACK chunk), this object is\nmeaningless. In such cases the object MUST contain a zero-\nlength string value. Otherwise, it contains the remote host\nname received at init time.")
sctpAssocLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 3), InetPortNumber().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocLocalPort.setDescription("The local SCTP port number used for this association.")
sctpAssocRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 4), InetPortNumber().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemPort.setDescription("The remote SCTP port number used for this association.")
sctpAssocRemPrimAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemPrimAddrType.setDescription("The internet type of primary remote IP address. ")
sctpAssocRemPrimAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemPrimAddr.setDescription("The primary remote IP address. The type of this address is\ndetermined by the value of sctpAssocRemPrimAddrType.\n\nThe client side will know this value after INIT_ACK message\nreception, the server side will know this value when sending\nINIT_ACK message. However, values will be filled in at\nestablished(4) state.")
sctpAssocHeartBeatInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 7), Unsigned32().clone(30000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocHeartBeatInterval.setDescription("The current heartbeat interval..\n\nZero value means no HeartBeat, even when the concerned\nsctpAssocRemAddrHBFlag object is true.")
sctpAssocState = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,4,2,6,9,1,8,7,3,)).subtype(namedValues=namedval.NamedValues(("closed", 1), ("cookieWait", 2), ("cookieEchoed", 3), ("established", 4), ("shutdownPending", 5), ("shutdownSent", 6), ("shutdownReceived", 7), ("shutdownAckSent", 8), ("deleteTCB", 9), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sctpAssocState.setDescription("The state of this SCTP association.\n\nAs in TCP, deleteTCB(9) is the only value that may be set by a\nmanagement station. If any other value is received, then the\nagent must return a wrongValue error.\n\nIf a management station sets this object to the value\ndeleteTCB(9), then this has the effect of deleting the TCB (as\ndefined in SCTP) of the corresponding association on the\nmanaged node, resulting in immediate termination of the\nassociation.\n\nAs an implementation-specific option, an ABORT chunk may be\nsent from the managed node to the other SCTP endpoint as a\nresult of setting the deleteTCB(9) value. The ABORT chunk\nimplies an ungraceful association shutdown.")
sctpAssocInStreams = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 9), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocInStreams.setDescription("Inbound Streams according to the negotiation at association\nstart up.")
sctpAssocOutStreams = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 10), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocOutStreams.setDescription("Outbound Streams according to the negotiation at association\nstart up. ")
sctpAssocMaxRetr = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 11), Unsigned32().clone(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocMaxRetr.setDescription("The maximum number of data retransmissions in the association\ncontext. This value is specific for each association and the\nupper layer can change it by calling the appropriate\nprimitives. This value has to be smaller than the addition of\nall the maximum number for all the paths\n(sctpAssocRemAddrMaxPathRtx).\n\n\n\nA value of zero value means no retransmissions.")
sctpAssocPrimProcess = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocPrimProcess.setDescription("This object identifies the system level process which holds\nprimary responsibility for the SCTP association.\nWherever possible, this should be the system's native unique\nidentification number. The special value 0 can be used to\nindicate that no primary process is known.\n\nNote that the value of this object can be used as a pointer\ninto the swRunTable of the HOST-RESOURCES-MIB(if the value is\nsmaller than 2147483647) or into the sysApplElmtRunTable of\nthe SYSAPPL-MIB.")
sctpAssocT1expireds = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocT1expireds.setDescription("The T1 timer determines how long to wait for an\nacknowledgement after sending an INIT or COOKIE-ECHO chunk.\nThis object reflects the number of times the T1 timer expires\nwithout having received the acknowledgement.\n\nDiscontinuities in the value of this counter can occur at re-\ninitialization of the management system, and at other times as\nindicated by the value of sctpAssocDiscontinuityTime.")
sctpAssocT2expireds = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocT2expireds.setDescription("The T2 timer determines how long to wait for an\nacknowledgement after sending a SHUTDOWN or SHUTDOWN-ACK\nchunk. This object reflects the number of times that T2- timer\nexpired.\n\nDiscontinuities in the value of this counter can occur at re-\ninitialization of the management system, and at other times as\nindicated by the value of sctpAssocDiscontinuityTime.")
sctpAssocRtxChunks = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRtxChunks.setDescription("When T3-rtx expires, the DATA chunks that triggered the T3\ntimer will be re-sent according with the retransmissions\nrules. Every DATA chunk that was included in the SCTP packet\nthat triggered the T3-rtx timer must be added to the value of\nthis counter.\n\nDiscontinuities in the value of this counter can occur at re-\ninitialization of the management system, and at other times as\nindicated by the value of sctpAssocDiscontinuityTime.")
sctpAssocStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 16), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocStartTime.setDescription("The value of sysUpTime at the time that the association\nrepresented by this row enters the ESTABLISHED state, i.e.,\nthe sctpAssocState object is set to established(4). The\nvalue of this object will be zero:\n- before the association enters the established(4)\n  state, or\n\n\n\n\n- if the established(4) state was entered prior to\n  the last re-initialization of the local network management\n  subsystem.")
sctpAssocDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 17), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which\nany one or more of this SCTP association counters suffered a\ndiscontinuity.  The relevant counters are the specific\ninstances associated with this interface of any Counter32 or\nCounter64 object contained in the sctpAssocTable or\nsctpLocalAddrTable or sctpRemAddrTable.  If no such\ndiscontinuities have occurred since the last re-initialization\nof the local management subsystem, then this object contains a\nzero value. ")
sctpAssocLocalAddrTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 4))
if mibBuilder.loadTexts: sctpAssocLocalAddrTable.setDescription("Expanded table of sctpAssocTable based on the AssocId index.\nThis table shows data related to each local IP address which\nis used by this association.")
sctpAssocLocalAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 4, 1)).setIndexNames((0, "SCTP-MIB", "sctpAssocId"), (0, "SCTP-MIB", "sctpAssocLocalAddrType"), (0, "SCTP-MIB", "sctpAssocLocalAddr"))
if mibBuilder.loadTexts: sctpAssocLocalAddrEntry.setDescription("Local information about the available addresses. There will\nbe an entry for every local IP address defined for this\n\n\n\nassociation.\nImplementors need to be aware that if the size of\nsctpAssocLocalAddr exceeds 114 octets then OIDs of column\ninstances in this table will have more than 128 sub-\nidentifiers and cannot be accessed using SNMPv1, SNMPv2c, or\nSNMPv3.")
sctpAssocLocalAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 4, 1, 1), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sctpAssocLocalAddrType.setDescription("Internet type of local IP address used for this association.")
sctpAssocLocalAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 4, 1, 2), InetAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sctpAssocLocalAddr.setDescription("The value of a local IP address available for this\nassociation. The type of this address is determined by the\nvalue of sctpAssocLocalAddrType.")
sctpAssocLocalAddrStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 4, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocLocalAddrStartTime.setDescription("The value of sysUpTime at the time that this row was\ncreated.")
sctpAssocRemAddrTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 5))
if mibBuilder.loadTexts: sctpAssocRemAddrTable.setDescription("Expanded table of sctpAssocTable based on the AssocId index.\nThis table shows data related to each remote peer IP address\nwhich is used by this association.")
sctpAssocRemAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 5, 1)).setIndexNames((0, "SCTP-MIB", "sctpAssocId"), (0, "SCTP-MIB", "sctpAssocRemAddrType"), (0, "SCTP-MIB", "sctpAssocRemAddr"))
if mibBuilder.loadTexts: sctpAssocRemAddrEntry.setDescription("Information about the most important variables for every\nremote IP address. There will be an entry for every remote IP\naddress defined for this association.\n\nImplementors need to be aware that if the size of\nsctpAssocRemAddr exceeds 114 octets then OIDs of column\ninstances in this table will have more than 128 sub-\nidentifiers and cannot be accessed using SNMPv1, SNMPv2c, or\nSNMPv3.")
sctpAssocRemAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 1), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sctpAssocRemAddrType.setDescription("Internet type of a remote IP address available for this\nassociation.")
sctpAssocRemAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 2), InetAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sctpAssocRemAddr.setDescription("The value of a remote IP address available for this\nassociation. The type of this address is determined by the\nvalue of sctpAssocLocalAddrType.")
sctpAssocRemAddrActive = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemAddrActive.setDescription("This object gives information about the reachability of this\nspecific remote IP address.\n\nWhen the object is set to 'true' (1), the remote IP address is\nunderstood as Active. Active means that the threshold of no\nanswers received from this IP address has not been reached.\n\n\n\n\n\n\nWhen the object is set to 'false' (2), the remote IP address\nis understood as Inactive. Inactive means that either no\nheartbeat or any other message was received from this address,\nreaching the threshold defined by the protocol.")
sctpAssocRemAddrHBActive = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemAddrHBActive.setDescription("This object indicates whether the optional Heartbeat check\nassociated to one destination transport address is activated\nor not (value equal to true or false, respectively). ")
sctpAssocRemAddrRTO = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemAddrRTO.setDescription("The current Retransmission Timeout. T3-rtx timer as defined\nin the protocol SCTP.")
sctpAssocRemAddrMaxPathRtx = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 6), Unsigned32().clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemAddrMaxPathRtx.setDescription("Maximum number of DATA chunks retransmissions allowed to a\nremote IP address before it is considered inactive, as defined\nin RFC2960.")
sctpAssocRemAddrRtx = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemAddrRtx.setDescription("Number of DATA chunks retransmissions to this specific IP\naddress. When T3-rtx expires, the DATA chunk that triggered\nthe T3 timer will be re-sent according to the retransmissions\nrules. Every DATA chunk that is included in a SCTP packet and\nwas transmitted to this specific IP address before, will be\nincluded in this counter.\n\nDiscontinuities in the value of this counter can occur at re-\ninitialization of the management system, and at other times as\nindicated by the value of sctpAssocDiscontinuityTime.")
sctpAssocRemAddrStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemAddrStartTime.setDescription("The value of sysUpTime at the time that this row was\ncreated.")
sctpLookupLocalPortTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 6))
if mibBuilder.loadTexts: sctpLookupLocalPortTable.setDescription("With the use of this table, a list of associations which are\n\n\n\nusing the specified local port can be retrieved.")
sctpLookupLocalPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 6, 1)).setIndexNames((0, "SCTP-MIB", "sctpAssocLocalPort"), (0, "SCTP-MIB", "sctpAssocId"))
if mibBuilder.loadTexts: sctpLookupLocalPortEntry.setDescription("This table is indexed by local port and association ID.\nSpecifying a local port, we would get a list of the\nassociations whose local port is the one specified.")
sctpLookupLocalPortStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 6, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpLookupLocalPortStartTime.setDescription("The value of sysUpTime at the time that this row was created.\n\nAs the table will be created after the sctpAssocTable\ncreation, this value could be equal to the sctpAssocStartTime\nobject from the main table.")
sctpLookupRemPortTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 7))
if mibBuilder.loadTexts: sctpLookupRemPortTable.setDescription("With the use of this table, a list of associations which are\nusing the specified remote port can be got")
sctpLookupRemPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 7, 1)).setIndexNames((0, "SCTP-MIB", "sctpAssocRemPort"), (0, "SCTP-MIB", "sctpAssocId"))
if mibBuilder.loadTexts: sctpLookupRemPortEntry.setDescription("This table is indexed by remote port and association ID.\nSpecifying a remote port we would get a list of the\nassociations whose local port is the one specified ")
sctpLookupRemPortStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 7, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpLookupRemPortStartTime.setDescription("The value of sysUpTime at the time that this row was created.\n\nAs the table will be created after the sctpAssocTable\ncreation, this value could be equal to the sctpAssocStartTime\nobject from the main table.")
sctpLookupRemHostNameTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 8))
if mibBuilder.loadTexts: sctpLookupRemHostNameTable.setDescription("With the use of this table, a list of associations with that\nparticular host can be retrieved.")
sctpLookupRemHostNameEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 8, 1)).setIndexNames((0, "SCTP-MIB", "sctpAssocRemHostName"), (0, "SCTP-MIB", "sctpAssocId"))
if mibBuilder.loadTexts: sctpLookupRemHostNameEntry.setDescription("This table is indexed by remote host name and association ID.\nSpecifying a host name we would get a list of the associations\nspecifying that host name as the remote one.\n\nImplementors need to be aware that if the size of\nsctpAssocRemHostName exceeds 115 octets then OIDs of column\ninstances in this table will have more than 128 sub-\nidentifiers and cannot be accessed using SNMPv1, SNMPv2c, or\nSNMPv3.")
sctpLookupRemHostNameStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 8, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpLookupRemHostNameStartTime.setDescription("The value of sysUpTime at the time that this row was created.\n\nAs the table will be created after the sctpAssocTable\ncreation, this value could be equal to the sctpAssocStartTime\nobject from the main table.")
sctpLookupRemPrimIPAddrTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 9))
if mibBuilder.loadTexts: sctpLookupRemPrimIPAddrTable.setDescription("With the use of this table, a list of associations that have\nthe specified IP address as primary within the remote set of\nactive addresses can be retrieved.")
sctpLookupRemPrimIPAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 9, 1)).setIndexNames((0, "SCTP-MIB", "sctpAssocRemPrimAddrType"), (0, "SCTP-MIB", "sctpAssocRemPrimAddr"), (0, "SCTP-MIB", "sctpAssocId"))
if mibBuilder.loadTexts: sctpLookupRemPrimIPAddrEntry.setDescription("This table is indexed by primary address and association ID.\nSpecifying a primary address, we would get a list of the\nassociations that have the specified remote IP address marked\nas primary.\nImplementors need to be aware that if the size of\nsctpAssocRemPrimAddr exceeds 114 octets then OIDs of column\ninstances in this table will have more than 128 sub-\nidentifiers and cannot be accessed using SNMPv1, SNMPv2c, or\nSNMPv3.")
sctpLookupRemPrimIPAddrStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 9, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpLookupRemPrimIPAddrStartTime.setDescription("The value of SysUpTime at the time that this row was created.\n\nAs the table will be created after the sctpAssocTable\ncreation, this value could be equal to the sctpAssocStartTime\nobject from the main table.")
sctpLookupRemIPAddrTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 10))
if mibBuilder.loadTexts: sctpLookupRemIPAddrTable.setDescription("With the use of this table, a list of associations that have\nthe specified IP address as one of the remote ones can be\nretrieved. ")
sctpLookupRemIPAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 10, 1)).setIndexNames((0, "SCTP-MIB", "sctpAssocRemAddrType"), (0, "SCTP-MIB", "sctpAssocRemAddr"), (0, "SCTP-MIB", "sctpAssocId"))
if mibBuilder.loadTexts: sctpLookupRemIPAddrEntry.setDescription("This table is indexed by a remote IP address and association\nID. Specifying an IP address we would get a list of the\nassociations that have the specified IP address included\nwithin the set of remote IP addresses.")
sctpLookupRemIPAddrStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 10, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpLookupRemIPAddrStartTime.setDescription("The value of SysUpTime at the time that this row was created.\n\nAs the table will be created after the sctpAssocTable\ncreation, this value could be equal to the sctpAssocStartTime\nobject from the main table.")
sctpMibConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 104, 2))
sctpMibCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 104, 2, 1))
sctpMibGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 104, 2, 2))

# Augmentions

# Groups

sctpLayerParamsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 104, 2, 2, 1)).setObjects(("SCTP-MIB", "sctpMaxAssocs"), ("SCTP-MIB", "sctpValCookieLife"), ("SCTP-MIB", "sctpRtoMin"), ("SCTP-MIB", "sctpMaxInitRetr"), ("SCTP-MIB", "sctpRtoInitial"), ("SCTP-MIB", "sctpRtoAlgorithm"), ("SCTP-MIB", "sctpRtoMax"), )
sctpPerAssocStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 104, 2, 2, 4)).setObjects(("SCTP-MIB", "sctpAssocRemAddrRtx"), ("SCTP-MIB", "sctpAssocT1expireds"), ("SCTP-MIB", "sctpAssocT2expireds"), ("SCTP-MIB", "sctpAssocRtxChunks"), )
sctpPerAssocParamsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 104, 2, 2, 3)).setObjects(("SCTP-MIB", "sctpAssocInStreams"), ("SCTP-MIB", "sctpAssocHeartBeatInterval"), ("SCTP-MIB", "sctpAssocRemAddrRTO"), ("SCTP-MIB", "sctpAssocDiscontinuityTime"), ("SCTP-MIB", "sctpAssocRemPrimAddrType"), ("SCTP-MIB", "sctpAssocRemAddrActive"), ("SCTP-MIB", "sctpAssocRemAddrHBActive"), ("SCTP-MIB", "sctpAssocRemAddrMaxPathRtx"), ("SCTP-MIB", "sctpAssocLocalPort"), ("SCTP-MIB", "sctpAssocState"), ("SCTP-MIB", "sctpAssocRemPort"), ("SCTP-MIB", "sctpAssocPrimProcess"), ("SCTP-MIB", "sctpAssocMaxRetr"), ("SCTP-MIB", "sctpAssocLocalAddrStartTime"), ("SCTP-MIB", "sctpAssocStartTime"), ("SCTP-MIB", "sctpAssocRemAddrStartTime"), ("SCTP-MIB", "sctpAssocOutStreams"), ("SCTP-MIB", "sctpAssocRemPrimAddr"), ("SCTP-MIB", "sctpAssocRemHostName"), )
sctpStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 104, 2, 2, 2)).setObjects(("SCTP-MIB", "sctpAborteds"), ("SCTP-MIB", "sctpOutUnorderChunks"), ("SCTP-MIB", "sctpDiscontinuityTime"), ("SCTP-MIB", "sctpChecksumErrors"), ("SCTP-MIB", "sctpAssocT1expireds"), ("SCTP-MIB", "sctpOutSCTPPacks"), ("SCTP-MIB", "sctpAssocRtxChunks"), ("SCTP-MIB", "sctpActiveEstabs"), ("SCTP-MIB", "sctpInCtrlChunks"), ("SCTP-MIB", "sctpInOrderChunks"), ("SCTP-MIB", "sctpOutOrderChunks"), ("SCTP-MIB", "sctpInSCTPPacks"), ("SCTP-MIB", "sctpReasmUsrMsgs"), ("SCTP-MIB", "sctpAssocRemAddrRtx"), ("SCTP-MIB", "sctpOutCtrlChunks"), ("SCTP-MIB", "sctpOutOfBlues"), ("SCTP-MIB", "sctpCurrEstab"), ("SCTP-MIB", "sctpPassiveEstabs"), ("SCTP-MIB", "sctpShutdowns"), ("SCTP-MIB", "sctpAssocT2expireds"), ("SCTP-MIB", "sctpFragUsrMsgs"), ("SCTP-MIB", "sctpInUnorderChunks"), )
sctpInverseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 104, 2, 2, 5)).setObjects(("SCTP-MIB", "sctpLookupRemHostNameStartTime"), ("SCTP-MIB", "sctpLookupRemIPAddrStartTime"), ("SCTP-MIB", "sctpLookupRemPortStartTime"), ("SCTP-MIB", "sctpLookupLocalPortStartTime"), ("SCTP-MIB", "sctpLookupRemPrimIPAddrStartTime"), )

# Exports

# Module identity
mibBuilder.exportSymbols("SCTP-MIB", PYSNMP_MODULE_ID=sctpMIB)

# Objects
mibBuilder.exportSymbols("SCTP-MIB", sctpMIB=sctpMIB, sctpObjects=sctpObjects, sctpStats=sctpStats, sctpCurrEstab=sctpCurrEstab, sctpActiveEstabs=sctpActiveEstabs, sctpPassiveEstabs=sctpPassiveEstabs, sctpAborteds=sctpAborteds, sctpShutdowns=sctpShutdowns, sctpOutOfBlues=sctpOutOfBlues, sctpChecksumErrors=sctpChecksumErrors, sctpOutCtrlChunks=sctpOutCtrlChunks, sctpOutOrderChunks=sctpOutOrderChunks, sctpOutUnorderChunks=sctpOutUnorderChunks, sctpInCtrlChunks=sctpInCtrlChunks, sctpInOrderChunks=sctpInOrderChunks, sctpInUnorderChunks=sctpInUnorderChunks, sctpFragUsrMsgs=sctpFragUsrMsgs, sctpReasmUsrMsgs=sctpReasmUsrMsgs, sctpOutSCTPPacks=sctpOutSCTPPacks, sctpInSCTPPacks=sctpInSCTPPacks, sctpDiscontinuityTime=sctpDiscontinuityTime, sctpParams=sctpParams, sctpRtoAlgorithm=sctpRtoAlgorithm, sctpRtoMin=sctpRtoMin, sctpRtoMax=sctpRtoMax, sctpRtoInitial=sctpRtoInitial, sctpMaxAssocs=sctpMaxAssocs, sctpValCookieLife=sctpValCookieLife, sctpMaxInitRetr=sctpMaxInitRetr, sctpAssocTable=sctpAssocTable, sctpAssocEntry=sctpAssocEntry, sctpAssocId=sctpAssocId, sctpAssocRemHostName=sctpAssocRemHostName, sctpAssocLocalPort=sctpAssocLocalPort, sctpAssocRemPort=sctpAssocRemPort, sctpAssocRemPrimAddrType=sctpAssocRemPrimAddrType, sctpAssocRemPrimAddr=sctpAssocRemPrimAddr, sctpAssocHeartBeatInterval=sctpAssocHeartBeatInterval, sctpAssocState=sctpAssocState, sctpAssocInStreams=sctpAssocInStreams, sctpAssocOutStreams=sctpAssocOutStreams, sctpAssocMaxRetr=sctpAssocMaxRetr, sctpAssocPrimProcess=sctpAssocPrimProcess, sctpAssocT1expireds=sctpAssocT1expireds, sctpAssocT2expireds=sctpAssocT2expireds, sctpAssocRtxChunks=sctpAssocRtxChunks, sctpAssocStartTime=sctpAssocStartTime, sctpAssocDiscontinuityTime=sctpAssocDiscontinuityTime, sctpAssocLocalAddrTable=sctpAssocLocalAddrTable, sctpAssocLocalAddrEntry=sctpAssocLocalAddrEntry, sctpAssocLocalAddrType=sctpAssocLocalAddrType, sctpAssocLocalAddr=sctpAssocLocalAddr, sctpAssocLocalAddrStartTime=sctpAssocLocalAddrStartTime, sctpAssocRemAddrTable=sctpAssocRemAddrTable, sctpAssocRemAddrEntry=sctpAssocRemAddrEntry, sctpAssocRemAddrType=sctpAssocRemAddrType, sctpAssocRemAddr=sctpAssocRemAddr, sctpAssocRemAddrActive=sctpAssocRemAddrActive, sctpAssocRemAddrHBActive=sctpAssocRemAddrHBActive, sctpAssocRemAddrRTO=sctpAssocRemAddrRTO, sctpAssocRemAddrMaxPathRtx=sctpAssocRemAddrMaxPathRtx, sctpAssocRemAddrRtx=sctpAssocRemAddrRtx, sctpAssocRemAddrStartTime=sctpAssocRemAddrStartTime, sctpLookupLocalPortTable=sctpLookupLocalPortTable, sctpLookupLocalPortEntry=sctpLookupLocalPortEntry, sctpLookupLocalPortStartTime=sctpLookupLocalPortStartTime, sctpLookupRemPortTable=sctpLookupRemPortTable, sctpLookupRemPortEntry=sctpLookupRemPortEntry, sctpLookupRemPortStartTime=sctpLookupRemPortStartTime, sctpLookupRemHostNameTable=sctpLookupRemHostNameTable, sctpLookupRemHostNameEntry=sctpLookupRemHostNameEntry, sctpLookupRemHostNameStartTime=sctpLookupRemHostNameStartTime, sctpLookupRemPrimIPAddrTable=sctpLookupRemPrimIPAddrTable, sctpLookupRemPrimIPAddrEntry=sctpLookupRemPrimIPAddrEntry, sctpLookupRemPrimIPAddrStartTime=sctpLookupRemPrimIPAddrStartTime, sctpLookupRemIPAddrTable=sctpLookupRemIPAddrTable, sctpLookupRemIPAddrEntry=sctpLookupRemIPAddrEntry, sctpLookupRemIPAddrStartTime=sctpLookupRemIPAddrStartTime, sctpMibConformance=sctpMibConformance, sctpMibCompliances=sctpMibCompliances, sctpMibGroups=sctpMibGroups)

# Groups
mibBuilder.exportSymbols("SCTP-MIB", sctpLayerParamsGroup=sctpLayerParamsGroup, sctpPerAssocStatsGroup=sctpPerAssocStatsGroup, sctpPerAssocParamsGroup=sctpPerAssocParamsGroup, sctpStatsGroup=sctpStatsGroup, sctpInverseGroup=sctpInverseGroup)
