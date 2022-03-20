
class ValueSet:
    _value_set = {
        "Branching.Type": ["Exclusive", "Parallel"],
        "RelativeTimingConstraint.Type": ["StartToStart", "StartToFinish", "FinishToStart", "FinishToFinish"],
        "PDFPageRef.Type": ["NamedDestination", "PhysicalRef"],
        "Origin.Type": ["Collected", "Derived", "Assigned", "Protocol", "Not Available"],
        "Origin.Source": ["Subject", "Investigator", "Vendor", "Sponsor"],
        "RangeCheck.Comparator": ["LT", "LE", "GT", "GE", "EQ", "NE", "IN", "NOTIN"],
        "RangeCheck.SoftHard": ["Soft", "Hard"],
        "StudyEventDef.Repeating": ["Yes", "No"],
        "CodeListItem.ExtendedValue": ["Yes"],
        "EnumeratedItem.ExtendedValue": ["Yes"],
        "FormDef.Repeating": ["Yes", "No"],
        "ItemGroupDef.Repeating": ["Yes", "No"],
        "ItemGroupDef.Type": ["Form", "Dataset", "Concept"],
        "FormRef.Mandatory": ["Yes", "No"],
        "ItemGroupRef.Mandatory": ["Yes", "No"],
        "StudyEventGroupRef.Mandatory": ["Yes", "No"],
        "ItemRef.Mandatory": ["Yes", "No"],
        "StudyEventRef.Mandatory": ["Yes", "No"],
        "ItemGroupDef.IsReferenceData": ["Yes", "No"],
        "ItemDef.DataType": ["text", "integer", "float", "date", "time", "datetime", "string", "boolean", "double",
                             "hexBinary", "base64Binary", "hexFloat", "base64Float", "partialDate", "partialTime",
                             "partialDatetime", "durationDatetime", "intervalDatetime", "incompleteDatetime",
                             "incompleteDate", "incompleteTime", "URI"],
        "Parameter.DataType": ["text", "integer", "float", "date", "time", "datetime", "string", "boolean", "double",
                             "hexBinary", "base64Binary", "hexFloat", "base64Float", "partialDate", "partialTime",
                             "partialDatetime", "durationDatetime", "intervalDatetime", "incompleteDatetime",
                             "incompleteDate", "incompleteTime", "URI"],
        "CodeList.DataType": ["integer", "float", "text", "string"],
        "MethodDef.Type": ["Computation", "Imputation", "Transpose", "Other"],
        "StudyEventDef.Type": ["Scheduled", "Unscheduled", "Common"],
        "ODM.FileType": ["Snapshot", "Transactional"],
        "ODM.Granularity": ["All", "Metadata", "AdminData", "ReferenceData", "AllClinicalData", "SingleSite",
                            "SingleSubject"],
        "ODM.Archival": ["Yes", "No"],
        "ODM.ODMVersion": ["1.2", "1.2.1", "1.3", "1.3.1", "1.3.2", "2.0"],
        "User.UserType": ["Sponsor", "Investigator", "Lab", "Other"],
        "Location.LocationType": ["Sponsor", "Site", "CRO", "Lab", "Other"],
        "SignatureDef.Methodology": ["Digital", "Electronic"],
        "Country._content": ['AF', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ',
                             'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BO', 'BA', 'BW', 'BV',
                             'BR', 'IO', 'BN', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL',
                             'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'CI', 'HR', 'CU', 'CY', 'CZ',
                             'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI',
                             'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU',
                             'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR',
                             'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KR',
                             'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG',
                             'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN',
                             'ME', 'MS', 'MA', 'MZ', 'MM', 'MM', 'NA', 'NR', 'NP', 'NL', 'AN', 'NC', 'NZ', 'NI', 'NE',
                             'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN',
                             'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RU', 'RW', 'SH', 'KN', 'LC', 'PM', 'VC', 'VC',
                             'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SK', 'SI', 'SB', 'SO', 'ZA',
                             'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TW', 'TJ', 'TZ',
                             'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB',
                             'US', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VE', 'VN', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM',
                             'ZW']
    }

    @classmethod
    def value_set(cls, attribute):
        if attribute in cls._value_set:
            return cls._value_set[attribute]
        else:
            raise ValueError(f"Unknown value {attribute} in ValueSet. Unable to check value.")