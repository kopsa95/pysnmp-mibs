# PySNMP SMI module. Autogenerated from smidump -f python DOCS-IETF-SUBMGT-MIB
# by libsmi2pysnmp-0.0.9-alpha at Fri Jul  9 17:12:38 2010,
# Python version sys.version_info(major=2, minor=7, micro=0, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( diffServActionStorage, diffServAlgDropStatus, diffServAlgDropStorage, diffServAlgDropType, diffServClfrElementStatus, diffServClfrElementStorage, diffServClfrStatus, diffServClfrStorage, diffServCountActStorage, diffServDataPathStatus, diffServDataPathStorage, diffServMIBActionGroup, diffServMIBAlgDropGroup, diffServMIBClfrElementGroup, diffServMIBClfrGroup, diffServMIBCounterGroup, diffServMIBDataPathGroup, diffServMIBMultiFieldClfrGroup, diffServMultiFieldClfrAddrType, diffServMultiFieldClfrDstAddr, diffServMultiFieldClfrSrcAddr, diffServMultiFieldClfrStorage, ) = mibBuilder.importSymbols("DIFFSERV-MIB", "diffServActionStorage", "diffServAlgDropStatus", "diffServAlgDropStorage", "diffServAlgDropType", "diffServClfrElementStatus", "diffServClfrElementStorage", "diffServClfrStatus", "diffServClfrStorage", "diffServCountActStorage", "diffServDataPathStatus", "diffServDataPathStorage", "diffServMIBActionGroup", "diffServMIBAlgDropGroup", "diffServMIBClfrElementGroup", "diffServMIBClfrGroup", "diffServMIBCounterGroup", "diffServMIBDataPathGroup", "diffServMIBMultiFieldClfrGroup", "diffServMultiFieldClfrAddrType", "diffServMultiFieldClfrDstAddr", "diffServMultiFieldClfrSrcAddr", "diffServMultiFieldClfrStorage")
( docsIfCmtsCmStatusEntry, docsIfCmtsCmStatusIndex, ) = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusEntry", "docsIfCmtsCmStatusIndex")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( RowStatus, StorageType, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TimeStamp", "TruthValue")

# Objects

docsSubMgt = ModuleIdentity((1, 3, 6, 1, 2, 1, 125)).setRevisions(("2005-03-29 00:00",))
if mibBuilder.loadTexts: docsSubMgt.setOrganization("IETF IP over Cable Data Network (IPCDN) Working\nGroup")
if mibBuilder.loadTexts: docsSubMgt.setContactInfo("        Wilson Sawyer\nPostal: 50 Kelly Brook Lane\n        East Hampstead, NH 03826\n        U.S.A.\n\nPhone:  +1 603 382 7080\nE-mail: wsawyer@ieee.org\n\nIETF IPCDN Working Group\nGeneral Discussion: ipcdn@ietf.org\nSubscribe: http://www.ietf.org/mailman/listinfo/ipcdn\nArchive: ftp://ftp.ietf.org/ietf-mail-archive/ipcdn\nCo-chairs: Richard Woundy, Richard_Woundy@cable.comcast.com\n           Jean-Francois Mule, jf.mule@cablelabs.com")
if mibBuilder.loadTexts: docsSubMgt.setDescription("This is the CMTS centric subscriber management MIB for\nDOCSIS-compliant CMTS.  It provides the objects to allow a Cable\nModem Termination operator to control the IP addresses and\nprotocols associated with subscribers' cable modems.\n\n\n\n\n\n\nCopyright (C) The Internet Society (2005).  This version of this\nMIB module is part of RFC 4036; see the RFC itself for full legal\nnotices.")
docsSubMgtObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 125, 1))
docsSubMgtCpeControlTable = MibTable((1, 3, 6, 1, 2, 1, 125, 1, 1))
if mibBuilder.loadTexts: docsSubMgtCpeControlTable.setDescription("This table AUGMENTs the docsIfCmtsCmStatusTable, adding\nfour WRITEable objects, as well as a read-only object, all of\nwhich reflect the state of subscriber management on a particular\nCM.")
docsSubMgtCpeControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 125, 1, 1, 1))
if mibBuilder.loadTexts: docsSubMgtCpeControlEntry.setDescription("A row in the docsSubMgtCpeControlTable.  All values are set\nat successful modem registration, either from the system default,\nor from objects included in the DOCSIS registration request sent\nupstream to the CMTS from the CM.  The contents of this entry are\nmeaningless unless the corresponding docsIfCmtsCmStatusValue (see\nreference) is registrationComplete(6).  The persistence of this\nrow is determined solely by the lifespan of the corresponding\ndocsIfCmtsCmStatusEntry (normally StorageType=volatile).")
docsSubMgtCpeControlMaxCpeIp = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeControlMaxCpeIp.setDescription("The number of simultaneous IP addresses permitted behind\nthe CM.  If this is set to zero, all CPE traffic from the CM is\ndropped.  If the provisioning object corresponding to\ndocsSubMgtCpeIpTable includes more CPE IP address entries for\nthis modem than the value of this object, then this object is\nset to the count of the number of rows in docsSubMgtCpeIpTable\nthat have the same docsIfCmtsCmStatusIndex value.  (For example,\nif the CM has 5 IP addresses specified for it, this value is 5.)\nThis limit applies to learned and DOCSIS-provisioned entries\nbut not to entries added through some administrative\nprocess at the CMTS.  If not set through DOCSIS provisioning,\nthis object defaults to docsSubMgtCpeMaxIpDefault.  Note that\nthis object is only meaningful if docsSubMgtCpeControlActive\nis true.")
docsSubMgtCpeControlActive = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeControlActive.setDescription("Controls the application of subscriber management to\nthis cable modem.  If this is set to true, CMTS-based CPE\ncontrol is active, and all the actions required by the various\nfilter tables and controls apply at the CMTS.  If this is set\nto false, no subscriber management filtering is done at the\nCMTS (but other filters may apply).  If not set through DOCSIS\nprovisioning, this object defaults to\ndocsSubMgtCpeActiveDefault.")
docsSubMgtCpeControlLearnable = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeControlLearnable.setDescription("Controls whether the CMTS may learn (and pass traffic\nfor) CPE IP addresses associated with a cable modem.  If this is\nset to true, the CMTS may learn up to docsSubMgtMaxCpeIp\n\n\n\naddresses (less any DOCSIS-provisioned entries) related to this\nCM.  Those IP addresses are added (by internal process) to the\ndocsSubMgtCpeIpTable.  The nature of the learning mechanism is\nnot specified here.\n\nIf not set through DOCSIS provisioning, this object defaults to\ndocsSubMgtCpeLearnableDefault.  Note that this object is only\nmeaningful if docsSubMgtCpeControlActive is true.")
docsSubMgtCpeControlReset = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeControlReset.setDescription("This object always returns false on read.  If this object is\nset to true, the rows with 'learned' addresses in\ndocsSubMgtCpeIpTable for this CM are deleted from that table.")
docsSubMgtCpeControlLastReset = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 1, 1, 5), TimeStamp().clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubMgtCpeControlLastReset.setDescription("The value of sysUpTime when docsSubMgtCpeControlReset was\nlast set true.  Zero if never reset.")
docsSubMgtCpeMaxIpDefault = MibScalar((1, 3, 6, 1, 2, 1, 125, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeMaxIpDefault.setDescription("The default value for docsSubMgtCpeControlMaxCpeIp if not\nsignaled in the DOCSIS Registration request.  This value should\nbe treated as nonvolatile; if set, its value should persist\nacross device resets.")
docsSubMgtCpeActiveDefault = MibScalar((1, 3, 6, 1, 2, 1, 125, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeActiveDefault.setDescription("The default value for docsSubMgtCpeControlActive if not\n\n\n\nsignaled in the DOCSIS Registration request.  This value should\nbe treated as nonvolatile; if set, its value should persist\nacross device resets.")
docsSubMgtCpeLearnableDefault = MibScalar((1, 3, 6, 1, 2, 1, 125, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCpeLearnableDefault.setDescription("The default value for docsSubMgtCpeControlLearnable if not\nsignaled in the DOCSIS Registration request.  This value should\nbe treated as nonvolatile; if set, its value should persist\nacross device resets.")
docsSubMgtCpeIpTable = MibTable((1, 3, 6, 1, 2, 1, 125, 1, 5))
if mibBuilder.loadTexts: docsSubMgtCpeIpTable.setDescription("A table of CPE IP addresses known on a per-CM basis.")
docsSubMgtCpeIpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 125, 1, 5, 1)).setIndexNames((0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"), (0, "DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeIpIndex"))
if mibBuilder.loadTexts: docsSubMgtCpeIpEntry.setDescription("An entry in the docsSubMgtCpeIpTable.  The first index is\nthe specific modem we're referring to, and the second index is\nthe specific CPE IP entry.")
docsSubMgtCpeIpIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: docsSubMgtCpeIpIndex.setDescription("The index of this CPE IP address relative to the indexed CM.\nAn entry is created either through the included CPE IP addresses\nin the provisioning object, or via learning.\n\nIf docsSubMgtCpeControlActive is true and a CMTS receives\nan IP packet from a CM that contains a source IP address that\ndoes not match one of the docsSubMgtCpeIpAddr entries for this\nCM, one of two things occurs.  If the number of entries is less\nthan docsSubMgtCpeControlMaxCpeIp, the source address is added to\nthe table and the packet is forwarded.  If the number of entries\nequals the docsSubMgtCpeControlMaxCpeIp, then the packet is\ndropped.")
docsSubMgtCpeIpAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 5, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubMgtCpeIpAddressType.setDescription("The type of internet address of docsSubMgtCpeIpAddr.")
docsSubMgtCpeIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 5, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubMgtCpeIpAddr.setDescription("The IP address either set from provisioning or learned via\naddress gleaning or other forwarding means.  See\ndocsSubMgtCpeIpIndex for the mechanism.\n\nThe type of this address is determined by the value of\ndocsSubMgtCpeIpAddressType.")
docsSubMgtCpeIpLearned = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 5, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubMgtCpeIpLearned.setDescription("If true, this entry was learned from IP packets sent\nupstream rather than from the provisioning objects.")
docsSubMgtCmFilterTable = MibTable((1, 3, 6, 1, 2, 1, 125, 1, 6))
if mibBuilder.loadTexts: docsSubMgtCmFilterTable.setDescription("Binds filter groups to modems, identifying for each modem\nthe upstream and downstream filter groups that apply to packets\nfor that modem.  Normally, this table reflects the filter group\nvalues signaled by DOCSIS Registration, although values may be\noverridden by management action.\n\nFor each of the columns in this table, zero is a distinguished\nvalue, indicating that the default filtering action is to be\ntaken rather than that associated with a filter group number.\nZero is used if the filter group is not signaled by DOCSIS\nregistration.")
docsSubMgtCmFilterEntry = MibTableRow((1, 3, 6, 1, 2, 1, 125, 1, 6, 1))
if mibBuilder.loadTexts: docsSubMgtCmFilterEntry.setDescription("Binds a filter group to each direction of traffic for a\nmodem.  The filters in this entry apply if\ndocsSubMgtCpeControlActive is true.\n\nThe contents of this entry are meaningless unless the\ncorresponding docsIfCmtsCmStatusValue (see reference) is\nregistrationComplete(6).  The persistence of this row is\ndetermined solely by the lifespan of the corresponding\ndocsIfCmtsCmStatusEntry (normally StorageType=volatile).")
docsSubMgtCmFilterSubDownstream = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCmFilterSubDownstream.setDescription("The filter group applied to traffic destined for subscribers\nattached to the referenced CM.  Upon row creation, this is set\neither to zero (use default classification, the\ndiffServClfrElementSpecific=zeroDotZero row of\ndiffServClfrElementTable) or to the value in the provisioning\nobject sent upstream from the CM to the CMTS during registration.\nThe value of this object is the same as that of the filter group\nindex appearing as docsSubMgtFilterGroupIndex.")
docsSubMgtCmFilterSubUpstream = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCmFilterSubUpstream.setDescription("The filter group applied to traffic originating from\nsubscribers attached to the referenced CM.  Upon row creation\nthis is set to either zero (use default classification, the\ndiffServClfrElementSpecific=zeroDotZero row of\ndiffServClfrElementTable), or to the value in the provisioning\nobject sent upstream from the CM to the CMTS.  The value of this\nobject is the same as that of the filter group index appearing as\ndocsSubMgtFilterGroupIndex.")
docsSubMgtCmFilterCmDownstream = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCmFilterCmDownstream.setDescription("The filter group applied to traffic destined for the\nreferenced CM itself.  Upon row creation this is set either to\nzero (use default classification, the\ndiffServClfrElementSpecific=zeroDotZero row of\ndiffServClfrElementTable), or to the value in the provisioning\nobject sent upstream from the CM to the CMTS during registration.\nThe value of this object is the same as that of the filter group\nindex appearing as docsSubMgtFilterGroupIndex.")
docsSubMgtCmFilterCmUpstream = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsSubMgtCmFilterCmUpstream.setDescription("The filter group applied to traffic originating from the\nreferenced CM itself.  This is set upon row creation to either\n\n\n\nzero (use default classification, the\ndiffServClfrElementSpecific=zeroDotZero row of\ndiffServClfrElementTable), or to the value in the provisioning\nobject sent upstream from the CM to the CMTS during registration.\nThe value of this object is the same as the filter group index\nappearing as docsSubMgtFilterGroupIndex.")
docsSubMgtFilterGroupTable = MibTable((1, 3, 6, 1, 2, 1, 125, 1, 7))
if mibBuilder.loadTexts: docsSubMgtFilterGroupTable.setDescription("Provides a collection of referenceable entries to which\ndiffServClfrElementSpecific refers.  This table provides filter\ngroup indices that can be compared with those signaled during\nDOCSIS registration.  A packet matches an entry from this table\nif the packet originated from or is destined to a cable modem\nthat registered this index as one of its four filter groups\n(see docsSubMgtCmFilterTable), and if the packet direction and\nMAC address select the use of this index among the four.")
docsSubMgtFilterGroupEntry = MibTableRow((1, 3, 6, 1, 2, 1, 125, 1, 7, 1)).setIndexNames((0, "DOCS-IETF-SUBMGT-MIB", "docsSubMgtFilterGroupIndex"))
if mibBuilder.loadTexts: docsSubMgtFilterGroupEntry.setDescription("An entry only exists if needed by the\ndiffServClfrElementEntry.  A packet matches this entry if the\npacket's cable modem registered this index as one of its four\nfilter groups (see docsSubMgtCmFilterTable) and if the packet\ndirection and MAC address select the use of this index among\nthe four.")
docsSubMgtFilterGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 125, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsSubMgtFilterGroupIndex.setDescription("The filter group index, from the set signaled at DOCSIS\n\n\n\nRegistration.  Provides a referenceable entry to which\ndiffServClfrElementSpecific points.  A packet matches this\nclassifier entry if the packet's cable modem registered this\nindex value as one of its four filter groups, and if the packet\ndirection and MAC address select the use of this index among\nthe four.  Because this is the only field in this table, it is\nread-only, contrary to the usual SMI custom of making indices\nnot-accessible.\n\nNote that although zero may be signaled (or defaulted) at DOCSIS\nRegistration to indicate a default filtering group, no such entry\nappears in this table, as diffServClfrElementSpecific will\nuse a zeroDotZero pointer for that classification.")
docsSubMgtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 125, 2))
docsSubMgtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 125, 2, 1))
docsSubMgtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 125, 2, 2))

# Augmentions
docsIfCmtsCmStatusEntry, = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusEntry")
docsIfCmtsCmStatusEntry.registerAugmentions(("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeControlEntry"))
apply(docsSubMgtCpeControlEntry.setIndexNames, docsIfCmtsCmStatusEntry.getIndexNames())
docsIfCmtsCmStatusEntry, = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusEntry")
docsIfCmtsCmStatusEntry.registerAugmentions(("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCmFilterEntry"))
apply(docsSubMgtCmFilterEntry.setIndexNames, docsIfCmtsCmStatusEntry.getIndexNames())

# Groups

docsSubMgtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 125, 2, 2, 1)).setObjects(("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCmFilterSubDownstream"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtFilterGroupIndex"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeControlReset"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeControlMaxCpeIp"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeMaxIpDefault"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeIpAddr"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeIpLearned"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeActiveDefault"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCmFilterCmUpstream"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCmFilterCmDownstream"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeControlActive"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCmFilterSubUpstream"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeIpAddressType"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeLearnableDefault"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeControlLastReset"), ("DOCS-IETF-SUBMGT-MIB", "docsSubMgtCpeControlLearnable"), )

# Exports

# Module identity
mibBuilder.exportSymbols("DOCS-IETF-SUBMGT-MIB", PYSNMP_MODULE_ID=docsSubMgt)

# Objects
mibBuilder.exportSymbols("DOCS-IETF-SUBMGT-MIB", docsSubMgt=docsSubMgt, docsSubMgtObjects=docsSubMgtObjects, docsSubMgtCpeControlTable=docsSubMgtCpeControlTable, docsSubMgtCpeControlEntry=docsSubMgtCpeControlEntry, docsSubMgtCpeControlMaxCpeIp=docsSubMgtCpeControlMaxCpeIp, docsSubMgtCpeControlActive=docsSubMgtCpeControlActive, docsSubMgtCpeControlLearnable=docsSubMgtCpeControlLearnable, docsSubMgtCpeControlReset=docsSubMgtCpeControlReset, docsSubMgtCpeControlLastReset=docsSubMgtCpeControlLastReset, docsSubMgtCpeMaxIpDefault=docsSubMgtCpeMaxIpDefault, docsSubMgtCpeActiveDefault=docsSubMgtCpeActiveDefault, docsSubMgtCpeLearnableDefault=docsSubMgtCpeLearnableDefault, docsSubMgtCpeIpTable=docsSubMgtCpeIpTable, docsSubMgtCpeIpEntry=docsSubMgtCpeIpEntry, docsSubMgtCpeIpIndex=docsSubMgtCpeIpIndex, docsSubMgtCpeIpAddressType=docsSubMgtCpeIpAddressType, docsSubMgtCpeIpAddr=docsSubMgtCpeIpAddr, docsSubMgtCpeIpLearned=docsSubMgtCpeIpLearned, docsSubMgtCmFilterTable=docsSubMgtCmFilterTable, docsSubMgtCmFilterEntry=docsSubMgtCmFilterEntry, docsSubMgtCmFilterSubDownstream=docsSubMgtCmFilterSubDownstream, docsSubMgtCmFilterSubUpstream=docsSubMgtCmFilterSubUpstream, docsSubMgtCmFilterCmDownstream=docsSubMgtCmFilterCmDownstream, docsSubMgtCmFilterCmUpstream=docsSubMgtCmFilterCmUpstream, docsSubMgtFilterGroupTable=docsSubMgtFilterGroupTable, docsSubMgtFilterGroupEntry=docsSubMgtFilterGroupEntry, docsSubMgtFilterGroupIndex=docsSubMgtFilterGroupIndex, docsSubMgtConformance=docsSubMgtConformance, docsSubMgtCompliances=docsSubMgtCompliances, docsSubMgtGroups=docsSubMgtGroups)

# Groups
mibBuilder.exportSymbols("DOCS-IETF-SUBMGT-MIB", docsSubMgtGroup=docsSubMgtGroup)
