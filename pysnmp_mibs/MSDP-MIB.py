# PySNMP SMI module. Autogenerated from smidump -f python MSDP-MIB
# by libsmi2pysnmp-0.0.9-alpha at Fri Jul  9 17:12:42 2010,
# Python version sys.version_info(major=2, minor=7, micro=0, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, experimental, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "experimental")
( DisplayString, RowStatus, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TimeStamp", "TruthValue")

# Objects

msdpMIB = ModuleIdentity((1, 3, 6, 1, 3, 92)).setRevisions(("2006-08-01 00:00",))
if mibBuilder.loadTexts: msdpMIB.setOrganization("IETF MBONED Working Group")
if mibBuilder.loadTexts: msdpMIB.setContactInfo("Bill Fenner\n75 Willow Road\nMenlo Park, CA  94025\nPhone: +1 650 867 6073\nE-mail: fenner@research.att.com\n\nDave Thaler\nOne Microsoft Way\nRedmond, WA  98052\nPhone: +1 425 703 8835\nEmail: dthaler@microsoft.com\n\nMBONED Working Group: mboned@lists.uoregon.edu")
if mibBuilder.loadTexts: msdpMIB.setDescription("An experimental MIB module for MSDP Management and\nMonitoring.\n\n\n\n\nCopyright (C) The Internet Society 2006.  This version of\nthis MIB module is part of RFC 4624; see the RFC itself\nfor full legal notices.")
msdpMIBobjects = MibIdentifier((1, 3, 6, 1, 3, 92, 1))
msdp = MibIdentifier((1, 3, 6, 1, 3, 92, 1, 1))
msdpTraps = MibIdentifier((1, 3, 6, 1, 3, 92, 1, 1, 0))
msdpEnabled = MibScalar((1, 3, 6, 1, 3, 92, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msdpEnabled.setDescription("The state of MSDP on this MSDP speaker - globally enabled\nor disabled.\n\nChanges to this object should be stored to non-volatile\nmemory.")
msdpCacheLifetime = MibScalar((1, 3, 6, 1, 3, 92, 1, 1, 2), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msdpCacheLifetime.setDescription("The lifetime given to SA cache entries when created or\nrefreshed.  This is the [SG-State-Period] in the MSDP\nspec.  A value of 0 means no SA caching is done by this\nMSDP speaker.\n\nChanges to this object should be stored to non-volatile\nmemory.\n\nThis object does not measure time per se; instead, it\nis the delta from the time at which an SA message is\nreceived at which it should be expired if not refreshed.\n(i.e., it is the value of msdpSACacheExpiryTime\nimmediately after receiving an SA message applying to\nthat row.)  As such, TimeInterval would be a more\nappropriate SYNTAX; it remains TimeTicks for backwards\ncompatibility.")
msdpNumSACacheEntries = MibScalar((1, 3, 6, 1, 3, 92, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpNumSACacheEntries.setDescription("The total number of entries in the SA Cache table.")
msdpRequestsTable = MibTable((1, 3, 6, 1, 3, 92, 1, 1, 4))
if mibBuilder.loadTexts: msdpRequestsTable.setDescription("The (conceptual) table listing group ranges and MSDP peers\nused when deciding where to send an SA Request message, when\nrequired.  If SA Requests are not enabled, this table may be\nempty.\n\nIn order to choose a peer to whom to send an SA Request for\na given group, G, the subset of entries in this table whose\n(msdpRequestsPeerType, msdpRequestsPeer) tuple represents a\n\n\n\npeer whose msdpPeerState is established are examined.  The\nset is further reduced by examining only those entries for\nwhich msdpPeerRequestsGroupAddressType equals the address\ntype of G.  The entries with the highest value of\nmsdpRequestsGroupPrefix are considered, where the group G\nfalls within the range described by the combination of\nmsdpRequestsGroup and msdpRequestsGroupPrefix.  (This\nsequence is commonly known as a 'longest-match' lookup.)\n\nFinally, if multiple entries remain, the entry with the\nlowest value of msdpRequestsPriority is chosen.  The SA\nRequest message is sent to the peer described by this row.")
msdpRequestsEntry = MibTableRow((1, 3, 6, 1, 3, 92, 1, 1, 4, 1)).setIndexNames((0, "MSDP-MIB", "msdpRequestsGroupAddress"), (0, "MSDP-MIB", "msdpRequestsGroupMask"))
if mibBuilder.loadTexts: msdpRequestsEntry.setDescription("An entry (conceptual row) representing a group range\nused when deciding where to send an SA Request\nmessage.")
msdpRequestsGroupAddress = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 1), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: msdpRequestsGroupAddress.setDescription("The group address that, when combined with the mask\nin this entry, represents the group range to which\nthis row applies.")
msdpRequestsGroupMask = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 2), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: msdpRequestsGroupMask.setDescription("The mask that, when combined with the group address\n\n\n\nin this entry, represents the group range to which\nthis row applies.")
msdpRequestsPeer = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpRequestsPeer.setDescription("The peer to which MSDP SA Requests for groups matching\nthis entry's group range will be sent.  This object,\ncombined with msdpRequestsPeerType, must match the INDEX\nof a row in the msdpPeerTable, and to be considered,\nthis peer's msdpPeerState must be established.")
msdpRequestsStatus = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpRequestsStatus.setDescription("The status of this row, by which new rows may be added\nto the table or old rows may be deleted.")
msdpPeerTable = MibTable((1, 3, 6, 1, 3, 92, 1, 1, 5))
if mibBuilder.loadTexts: msdpPeerTable.setDescription("The (conceptual) table listing the MSDP speaker's peers.")
msdpPeerEntry = MibTableRow((1, 3, 6, 1, 3, 92, 1, 1, 5, 1)).setIndexNames((0, "MSDP-MIB", "msdpPeerRemoteAddress"))
if mibBuilder.loadTexts: msdpPeerEntry.setDescription("An entry (conceptual row) representing an MSDP peer.\n\nIf row creation is supported, dynamically added rows are\nadded to the system's stable configuration (corresponding\nto a StorageType value of nonVolatile).  ")
msdpPeerRemoteAddress = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 1), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: msdpPeerRemoteAddress.setDescription("The address of the remote MSDP peer.")
msdpPeerState = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,5,1,3,2,)).subtype(namedValues=namedval.NamedValues(("inactive", 1), ("listen", 2), ("connecting", 3), ("established", 4), ("disabled", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerState.setDescription("The state of the MSDP TCP connection with this peer.")
msdpPeerRPFFailures = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerRPFFailures.setDescription("The number of SA messages received from this peer that\nfailed the Peer-RPF check.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\nmsdpPeerDiscontinuityTime.")
msdpPeerInSAs = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInSAs.setDescription("The number of MSDP SA messages received on this\nconnection.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\nmsdpPeerDiscontinuityTime.")
msdpPeerOutSAs = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerOutSAs.setDescription("The number of MSDP SA messages transmitted on this\nconnection.\n\n\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\nmsdpPeerDiscontinuityTime.")
msdpPeerInSARequests = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInSARequests.setDescription("The number of MSDP SA-Request messages received on this\nconnection.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\nmsdpPeerDiscontinuityTime.")
msdpPeerOutSARequests = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerOutSARequests.setDescription("The number of MSDP SA-Request messages transmitted on\nthis connection.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\nmsdpPeerDiscontinuityTime.")
msdpPeerInSAResponses = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInSAResponses.setDescription("The number of MSDP SA-Response messages received on this\nconnection.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\nmsdpPeerDiscontinuityTime.")
msdpPeerOutSAResponses = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerOutSAResponses.setDescription("The number of MSDP SA Response messages transmitted on\nthis TCP connection.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\nmsdpPeerDiscontinuityTime.")
msdpPeerInControlMessages = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInControlMessages.setDescription("The total number of MSDP messages, excluding encapsulated\ndata packets, received on this TCP connection.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\nmsdpPeerDiscontinuityTime.")
msdpPeerOutControlMessages = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerOutControlMessages.setDescription("The total number of MSDP messages, excluding encapsulated\ndata packets, transmitted on this TCP connection.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\nmsdpPeerDiscontinuityTime.")
msdpPeerInDataPackets = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInDataPackets.setDescription("The total number of encapsulated data packets received\n\n\n\nfrom this peer.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\nmsdpPeerDiscontinuityTime.")
msdpPeerOutDataPackets = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerOutDataPackets.setDescription("The total number of encapsulated data packets sent to\nthis peer.\n\nDiscontinuities in the value of this counter can occur at\nre-initialization of the management system, and at other\ntimes as indicated by the value of\nmsdpPeerDiscontinuityTime.")
msdpPeerFsmEstablishedTransitions = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerFsmEstablishedTransitions.setDescription("The total number of times the MSDP FSM transitioned into\nthe ESTABLISHED state.")
msdpPeerFsmEstablishedTime = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 16), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerFsmEstablishedTime.setDescription("This timestamp is set to the value of sysUpTime when a\npeer transitions into or out of the ESTABLISHED state.\nIt is set to zero when the MSDP speaker is booted.")
msdpPeerInMessageTime = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 17), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInMessageTime.setDescription("The sysUpTime value when the last MSDP message was\nreceived from the peer.  It is set to zero when the MSDP\nspeaker is booted.")
msdpPeerLocalAddress = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 18), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerLocalAddress.setDescription("The local IP address used for this entry's MSDP TCP\nconnection.")
msdpPeerConnectRetryInterval = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 20), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535)).clone(30)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerConnectRetryInterval.setDescription("Time interval, in seconds, for the [ConnectRetry-period]\nfor this peer.")
msdpPeerHoldTimeConfigured = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 21), Integer32().subtype(subtypeSpec=constraint.ConstraintsUnion(constraint.ValueRangeConstraint(0,0),constraint.ValueRangeConstraint(3,65535),)).clone(75)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerHoldTimeConfigured.setDescription("Time interval, in seconds, for the [HoldTime-Period]\nconfigured for this MSDP speaker with this peer.  If the\nvalue of this object is zero (0), the MSDP connection is\nnever torn down due to the absence of messages from the\npeer.")
msdpPeerKeepAliveConfigured = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 22), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 21845)).clone(60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerKeepAliveConfigured.setDescription("Time interval, in seconds, for the [KeepAlive-Period]\nconfigured for this MSDP speaker with this peer.  If the\nvalue of this object is zero (0), no periodic KEEPALIVE\nmessages are sent to the peer after the MSDP connection\nhas been established.")
msdpPeerDataTtl = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 23), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerDataTtl.setDescription("The minimum TTL a packet is required to have before it\nmay be forwarded using SA encapsulation to this peer.")
msdpPeerProcessRequestsFrom = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 24), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerProcessRequestsFrom.setDescription("This object indicates whether to process MSDP SA\nRequest messages from this peer.  If True(1), MSDP SA\nRequest messages from this peer are processed and replied\nto (if appropriate) with SA Response messages.  If\nFalse(2), MSDP SA Request messages from this peer are\nsilently ignored.  It defaults to False when\nmsdpCacheLifetime is 0 and to True when msdpCacheLifetime\nis non-0.\n\nThis object is deprecated because MSDP SA Requests were\nremoved from the MSDP specification.")
msdpPeerStatus = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 25), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerStatus.setDescription("The RowStatus object by which peers can be added and\ndeleted.  A transition to 'active' will cause the MSDP\n\n\n\n'Enable MSDP peering with P' Event to be generated.  A\ntransition out of the 'active' state will cause the MSDP\n'Disable MSDP peering with P' Event to be generated.\nCare should be used in providing write access to this\nobject without adequate authentication.\n\nmsdpPeerRemoteAddress is the only variable that must be\nset to a valid value before the row can be activated.\nSince this is the table's INDEX, a row can be activated\nby simply setting the msdpPeerStatus variable.\n\nIt is possible to modify other columns in the same\nconceptual row when the status value is active(1).")
msdpPeerRemotePort = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 26), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535)).clone(639)).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerRemotePort.setDescription("The remote port for the TCP connection between the MSDP\npeers.")
msdpPeerLocalPort = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 27), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535)).clone(639)).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerLocalPort.setDescription("The local port for the TCP connection between the MSDP\npeers.")
msdpPeerEncapsulationType = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 29), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(0,1,)).subtype(namedValues=namedval.NamedValues(("none", 0), ("tcp", 1), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpPeerEncapsulationType.setDescription("The encapsulation in use when encapsulating data in SA\nmessages to this peer.")
msdpPeerConnectionAttempts = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerConnectionAttempts.setDescription("The number of times the state machine has transitioned\nfrom INACTIVE to CONNECTING.")
msdpPeerInNotifications = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerInNotifications.setDescription("The number of MSDP Notification messages received from\nthis peer.\nThis object is deprecated because MSDP Notifications have\nbeen removed from the spec.")
msdpPeerOutNotifications = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerOutNotifications.setDescription("The number of MSDP Notification messages transmitted to\nthis peer.\n\nThis object is deprecated because MSDP Notifications have\nbeen removed from the spec.")
msdpPeerLastError = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 33), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 2)).setFixedLength(2).clone('\x00\x00')).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerLastError.setDescription("The last error code and subcode received via Notification\nfrom this peer.  If no error has occurred, this field is\nzero.  Otherwise, the first byte of this two-byte OCTET\nSTRING contains the O-bit and error code, and the second\nbyte contains the subcode.\n\n\n\n\nThis object is deprecated because MSDP Notifications have\nbeen removed from the spec.")
msdpPeerDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 34), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpPeerDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at\nwhich one or more of this entry's counters suffered a\ndiscontinuity.  See the DESCRIPTION of each object to see\nif it is expected to have discontinuities.  These\ndiscontinuities may occur at peer connection\nestablishment.\n\nIf no such discontinuities have occurred since the last\nreinitialization of the local management subsystem, then\nthis object contains a zero value.")
msdpSACacheTable = MibTable((1, 3, 6, 1, 3, 92, 1, 1, 6))
if mibBuilder.loadTexts: msdpSACacheTable.setDescription("The (conceptual) table listing the MSDP SA advertisements\ncurrently in the MSDP speaker's cache.")
msdpSACacheEntry = MibTableRow((1, 3, 6, 1, 3, 92, 1, 1, 6, 1)).setIndexNames((0, "MSDP-MIB", "msdpSACacheGroupAddr"), (0, "MSDP-MIB", "msdpSACacheSourceAddr"), (0, "MSDP-MIB", "msdpSACacheOriginRP"))
if mibBuilder.loadTexts: msdpSACacheEntry.setDescription("An entry (conceptual row) representing an MSDP SA\nadvertisement.  The INDEX to this table includes\nmsdpSACacheOriginRP for diagnosing incorrect MSDP\nadvertisements; normally, a Group and Source pair would\nbe unique.\n\nRow creation is not permitted; msdpSACacheStatus may only\nbe used to delete rows from this table.")
msdpSACacheGroupAddr = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 1), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: msdpSACacheGroupAddr.setDescription("The group address of the SA Cache entry.")
msdpSACacheSourceAddr = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 2), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: msdpSACacheSourceAddr.setDescription("The source address of the SA Cache entry.")
msdpSACacheOriginRP = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 3), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: msdpSACacheOriginRP.setDescription("The RP of the SA Cache entry.  This field is in the INDEX\nin order to catch multiple RP's advertising the same\nsource and group.")
msdpSACachePeerLearnedFrom = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSACachePeerLearnedFrom.setDescription("The peer from which this SA Cache entry was last\naccepted.  This address must correspond to the\nmsdpPeerRemoteAddress value for a row in the MSDP Peer\nTable.  This should be 0.0.0.0 on the router that\noriginated the entry.")
msdpSACacheRPFPeer = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSACacheRPFPeer.setDescription("The peer from which an SA message corresponding to this\ncache entry would be accepted (i.e., the RPF peer for\nmsdpSACacheOriginRP).  This may be different than\nmsdpSACachePeerLearnedFrom if this entry was created by\nan MSDP SA-Response.  This address must correspond to\nthe msdpPeerRemoteAddress value for a row in the MSDP\nPeer Table, or it may be 0.0.0.0 if no RPF peer exists.")
msdpSACacheInSAs = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSACacheInSAs.setDescription("The number of MSDP SA messages received relevant to this\ncache entry.  This object must be initialized to zero\nwhen creating a cache entry.")
msdpSACacheInDataPackets = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSACacheInDataPackets.setDescription("The number of MSDP-encapsulated data packets received\nrelevant to this cache entry.  This object must be\ninitialized to zero when creating a cache entry.")
msdpSACacheUpTime = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSACacheUpTime.setDescription("The time since this entry was first placed in the SA\ncache.\n\n\n\nThe first epoch is the time that the entry was first\nplaced in the SA cache, and the second epoch is the\ncurrent time.")
msdpSACacheExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: msdpSACacheExpiryTime.setDescription("The time remaining before this entry will expire from\nthe SA cache.\n\nThe first epoch is now, and the second epoch is the time\nthat the entry will expire.")
msdpSACacheStatus = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,6,)).subtype(namedValues=namedval.NamedValues(("active", 1), ("destroy", 6), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msdpSACacheStatus.setDescription("The status of this row in the table.  The only allowable\nactions are to retrieve the status, which will be\n'active', or to set the status to 'destroy' in order to\nremove this entry from the cache.\n\nRow creation is not permitted.\n\nNo columnar objects are writable, so there are none that\nmay be changed while the status value is active(1).")
msdpMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 92, 1, 1, 8))
msdpMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 92, 1, 1, 8, 1))
msdpMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 92, 1, 1, 8, 2))
msdpRPAddress = MibScalar((1, 3, 6, 1, 3, 92, 1, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msdpRPAddress.setDescription("The Rendezvous Point (RP) address used when sourcing\nMSDP SA messages.  May be 0.0.0.0 on non-RPs.\n\nChanges to this object should be stored to non-volatile\nmemory.")
msdpMeshGroupTable = MibTable((1, 3, 6, 1, 3, 92, 1, 1, 12))
if mibBuilder.loadTexts: msdpMeshGroupTable.setDescription("The (conceptual) table listing MSDP Mesh Group\nconfiguration.")
msdpMeshGroupEntry = MibTableRow((1, 3, 6, 1, 3, 92, 1, 1, 12, 1)).setIndexNames((0, "MSDP-MIB", "msdpMeshGroupName"), (0, "MSDP-MIB", "msdpMeshGroupPeerAddress"))
if mibBuilder.loadTexts: msdpMeshGroupEntry.setDescription("An entry (conceptual row) representing a peer in an MSDP\nMesh Group.\n\nIf row creation is supported, dynamically added rows are\nadded to the system's stable configuration\n(corresponding to a StorageType value of nonVolatile).")
msdpMeshGroupName = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 12, 1, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 64))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: msdpMeshGroupName.setDescription("The name of the mesh group.")
msdpMeshGroupPeerAddress = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 12, 1, 2), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: msdpMeshGroupPeerAddress.setDescription("A peer address that is a member of the mesh group with\nname msdpMeshGroupName.  The msdpMeshGroupPeerAddress\nmust match a row in the msdpPeerTable.")
msdpMeshGroupStatus = MibTableColumn((1, 3, 6, 1, 3, 92, 1, 1, 12, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: msdpMeshGroupStatus.setDescription("This entry's status, by which new entries may be added\nto the table and old entries deleted.\n\nmsdpMeshGroupName and msdpMeshGroupPeerAddress must be\nset to valid values before the row can be activated.\nSince these are the table's INDEX, a row can be activated\n\n\n\nby simply setting the msdpMeshGroupStatus variable.\n\nIt is not possible to modify other columns in the same\nconceptual row when the status value is active(1),\nbecause the only other objects in the row are part of the\nINDEX.  Changing one of these changes the row, so an old\nrow must be deleted and a new one created.")

# Augmentions

# Notifications

msdpBackwardTransition = NotificationType((1, 3, 6, 1, 3, 92, 1, 1, 0, 2)).setObjects(("MSDP-MIB", "msdpPeerState"), )
msdpEstablished = NotificationType((1, 3, 6, 1, 3, 92, 1, 1, 0, 1)).setObjects(("MSDP-MIB", "msdpPeerFsmEstablishedTransitions"), )

# Groups

msdpMIBMeshGroupGroup = ObjectGroup((1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 8)).setObjects(("MSDP-MIB", "msdpMeshGroupStatus"), )
msdpMIBSACacheGroup = ObjectGroup((1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 4)).setObjects(("MSDP-MIB", "msdpSACacheInDataPackets"), ("MSDP-MIB", "msdpNumSACacheEntries"), ("MSDP-MIB", "msdpSACachePeerLearnedFrom"), ("MSDP-MIB", "msdpSACacheStatus"), ("MSDP-MIB", "msdpCacheLifetime"), ("MSDP-MIB", "msdpSACacheUpTime"), ("MSDP-MIB", "msdpSACacheRPFPeer"), ("MSDP-MIB", "msdpSACacheInSAs"), ("MSDP-MIB", "msdpSACacheExpiryTime"), )
msdpMIBGlobalsGroup = ObjectGroup((1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 1)).setObjects(("MSDP-MIB", "msdpEnabled"), )
msdpMIBRequestsGroup = ObjectGroup((1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 6)).setObjects(("MSDP-MIB", "msdpRequestsPeer"), ("MSDP-MIB", "msdpRequestsStatus"), )
msdpMIBRPGroup = ObjectGroup((1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 7)).setObjects(("MSDP-MIB", "msdpRPAddress"), )
msdpMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 5)).setObjects(("MSDP-MIB", "msdpBackwardTransition"), ("MSDP-MIB", "msdpEstablished"), )
msdpMIBPeerGroup2 = ObjectGroup((1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 9)).setObjects(("MSDP-MIB", "msdpPeerLocalAddress"), ("MSDP-MIB", "msdpPeerOutSAs"), ("MSDP-MIB", "msdpPeerKeepAliveConfigured"), ("MSDP-MIB", "msdpPeerConnectionAttempts"), ("MSDP-MIB", "msdpPeerRPFFailures"), ("MSDP-MIB", "msdpPeerInSARequests"), ("MSDP-MIB", "msdpPeerInMessageTime"), ("MSDP-MIB", "msdpPeerOutSARequests"), ("MSDP-MIB", "msdpPeerLocalPort"), ("MSDP-MIB", "msdpPeerHoldTimeConfigured"), ("MSDP-MIB", "msdpPeerDiscontinuityTime"), ("MSDP-MIB", "msdpPeerFsmEstablishedTransitions"), ("MSDP-MIB", "msdpPeerState"), ("MSDP-MIB", "msdpPeerStatus"), ("MSDP-MIB", "msdpPeerInControlMessages"), ("MSDP-MIB", "msdpPeerConnectRetryInterval"), ("MSDP-MIB", "msdpPeerOutControlMessages"), ("MSDP-MIB", "msdpPeerRemotePort"), ("MSDP-MIB", "msdpPeerInSAs"), ("MSDP-MIB", "msdpPeerFsmEstablishedTime"), )
msdpMIBEncapsulationGroup = ObjectGroup((1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 3)).setObjects(("MSDP-MIB", "msdpPeerInDataPackets"), ("MSDP-MIB", "msdpPeerEncapsulationType"), ("MSDP-MIB", "msdpPeerOutDataPackets"), ("MSDP-MIB", "msdpPeerDataTtl"), )
msdpMIBPeerGroup = ObjectGroup((1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 2)).setObjects(("MSDP-MIB", "msdpPeerFsmEstablishedTime"), ("MSDP-MIB", "msdpPeerRPFFailures"), ("MSDP-MIB", "msdpPeerConnectionAttempts"), ("MSDP-MIB", "msdpPeerOutSARequests"), ("MSDP-MIB", "msdpPeerFsmEstablishedTransitions"), ("MSDP-MIB", "msdpPeerInControlMessages"), ("MSDP-MIB", "msdpPeerProcessRequestsFrom"), ("MSDP-MIB", "msdpPeerLastError"), ("MSDP-MIB", "msdpPeerLocalAddress"), ("MSDP-MIB", "msdpPeerLocalPort"), ("MSDP-MIB", "msdpPeerOutSAResponses"), ("MSDP-MIB", "msdpPeerConnectRetryInterval"), ("MSDP-MIB", "msdpPeerOutNotifications"), ("MSDP-MIB", "msdpPeerInNotifications"), ("MSDP-MIB", "msdpPeerDiscontinuityTime"), ("MSDP-MIB", "msdpPeerState"), ("MSDP-MIB", "msdpPeerStatus"), ("MSDP-MIB", "msdpPeerOutSAs"), ("MSDP-MIB", "msdpPeerInSARequests"), ("MSDP-MIB", "msdpPeerInMessageTime"), ("MSDP-MIB", "msdpPeerInSAs"), ("MSDP-MIB", "msdpPeerKeepAliveConfigured"), ("MSDP-MIB", "msdpPeerHoldTimeConfigured"), ("MSDP-MIB", "msdpPeerInSAResponses"), ("MSDP-MIB", "msdpPeerOutControlMessages"), ("MSDP-MIB", "msdpPeerRemotePort"), )

# Exports

# Module identity
mibBuilder.exportSymbols("MSDP-MIB", PYSNMP_MODULE_ID=msdpMIB)

# Objects
mibBuilder.exportSymbols("MSDP-MIB", msdpMIB=msdpMIB, msdpMIBobjects=msdpMIBobjects, msdp=msdp, msdpTraps=msdpTraps, msdpEnabled=msdpEnabled, msdpCacheLifetime=msdpCacheLifetime, msdpNumSACacheEntries=msdpNumSACacheEntries, msdpRequestsTable=msdpRequestsTable, msdpRequestsEntry=msdpRequestsEntry, msdpRequestsGroupAddress=msdpRequestsGroupAddress, msdpRequestsGroupMask=msdpRequestsGroupMask, msdpRequestsPeer=msdpRequestsPeer, msdpRequestsStatus=msdpRequestsStatus, msdpPeerTable=msdpPeerTable, msdpPeerEntry=msdpPeerEntry, msdpPeerRemoteAddress=msdpPeerRemoteAddress, msdpPeerState=msdpPeerState, msdpPeerRPFFailures=msdpPeerRPFFailures, msdpPeerInSAs=msdpPeerInSAs, msdpPeerOutSAs=msdpPeerOutSAs, msdpPeerInSARequests=msdpPeerInSARequests, msdpPeerOutSARequests=msdpPeerOutSARequests, msdpPeerInSAResponses=msdpPeerInSAResponses, msdpPeerOutSAResponses=msdpPeerOutSAResponses, msdpPeerInControlMessages=msdpPeerInControlMessages, msdpPeerOutControlMessages=msdpPeerOutControlMessages, msdpPeerInDataPackets=msdpPeerInDataPackets, msdpPeerOutDataPackets=msdpPeerOutDataPackets, msdpPeerFsmEstablishedTransitions=msdpPeerFsmEstablishedTransitions, msdpPeerFsmEstablishedTime=msdpPeerFsmEstablishedTime, msdpPeerInMessageTime=msdpPeerInMessageTime, msdpPeerLocalAddress=msdpPeerLocalAddress, msdpPeerConnectRetryInterval=msdpPeerConnectRetryInterval, msdpPeerHoldTimeConfigured=msdpPeerHoldTimeConfigured, msdpPeerKeepAliveConfigured=msdpPeerKeepAliveConfigured, msdpPeerDataTtl=msdpPeerDataTtl, msdpPeerProcessRequestsFrom=msdpPeerProcessRequestsFrom, msdpPeerStatus=msdpPeerStatus, msdpPeerRemotePort=msdpPeerRemotePort, msdpPeerLocalPort=msdpPeerLocalPort, msdpPeerEncapsulationType=msdpPeerEncapsulationType, msdpPeerConnectionAttempts=msdpPeerConnectionAttempts, msdpPeerInNotifications=msdpPeerInNotifications, msdpPeerOutNotifications=msdpPeerOutNotifications, msdpPeerLastError=msdpPeerLastError, msdpPeerDiscontinuityTime=msdpPeerDiscontinuityTime, msdpSACacheTable=msdpSACacheTable, msdpSACacheEntry=msdpSACacheEntry, msdpSACacheGroupAddr=msdpSACacheGroupAddr, msdpSACacheSourceAddr=msdpSACacheSourceAddr, msdpSACacheOriginRP=msdpSACacheOriginRP, msdpSACachePeerLearnedFrom=msdpSACachePeerLearnedFrom, msdpSACacheRPFPeer=msdpSACacheRPFPeer, msdpSACacheInSAs=msdpSACacheInSAs, msdpSACacheInDataPackets=msdpSACacheInDataPackets, msdpSACacheUpTime=msdpSACacheUpTime, msdpSACacheExpiryTime=msdpSACacheExpiryTime, msdpSACacheStatus=msdpSACacheStatus, msdpMIBConformance=msdpMIBConformance, msdpMIBCompliances=msdpMIBCompliances, msdpMIBGroups=msdpMIBGroups, msdpRPAddress=msdpRPAddress, msdpMeshGroupTable=msdpMeshGroupTable, msdpMeshGroupEntry=msdpMeshGroupEntry, msdpMeshGroupName=msdpMeshGroupName, msdpMeshGroupPeerAddress=msdpMeshGroupPeerAddress, msdpMeshGroupStatus=msdpMeshGroupStatus)

# Notifications
mibBuilder.exportSymbols("MSDP-MIB", msdpBackwardTransition=msdpBackwardTransition, msdpEstablished=msdpEstablished)

# Groups
mibBuilder.exportSymbols("MSDP-MIB", msdpMIBMeshGroupGroup=msdpMIBMeshGroupGroup, msdpMIBSACacheGroup=msdpMIBSACacheGroup, msdpMIBGlobalsGroup=msdpMIBGlobalsGroup, msdpMIBRequestsGroup=msdpMIBRequestsGroup, msdpMIBRPGroup=msdpMIBRPGroup, msdpMIBNotificationGroup=msdpMIBNotificationGroup, msdpMIBPeerGroup2=msdpMIBPeerGroup2, msdpMIBEncapsulationGroup=msdpMIBEncapsulationGroup, msdpMIBPeerGroup=msdpMIBPeerGroup)
