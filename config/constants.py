SERVICE_CATEGORY_ALLOTMENT = 'A'
SERVICE_CATEGORY_TRANSFER = 'T'
SERVICE_CATEGORY_DICT = {
    SERVICE_CATEGORY_ALLOTMENT : 'Allotment',
    SERVICE_CATEGORY_TRANSFER : 'Transfer',
}
SERVICE_CATEGORIES = (
    (SERVICE_CATEGORY_ALLOTMENT, SERVICE_CATEGORY_DICT[SERVICE_CATEGORY_ALLOTMENT]),
    (SERVICE_CATEGORY_TRANSFER, SERVICE_CATEGORY_DICT[SERVICE_CATEGORY_TRANSFER]),
)

TRANSPORT_COST_TYPE_BYPAX = 'P'
TRANSPORT_COST_TYPE_BYTRANSPORT = 'T'
TRANSPORT_COST_TYPES = (
    (TRANSPORT_COST_TYPE_BYPAX, 'By Pax'),
    (TRANSPORT_COST_TYPE_BYTRANSPORT, 'By Transport'),
)

TRANSPORT_SUPPLEMENT_COST_TYPE_BYHOUR = 'H'
TRANSPORT_SUPPLEMENT_COST_TYPE_BYTRANSPORT = 'T'
TRANSPORT_SUPPLEMENT_COST_TYPES = (
    (TRANSPORT_SUPPLEMENT_COST_TYPE_BYHOUR, 'By Hour'),
    (TRANSPORT_SUPPLEMENT_COST_TYPE_BYTRANSPORT, 'By Transport'),
)

ALLOTMENT_SUPPLEMENT_COST_TYPE_FIXED = 'F'
ALLOTMENT_SUPPLEMENT_COST_TYPE_BYPAXES = 'P'
ALLOTMENT_SUPPLEMENT_COST_TYPE_BYDAYS = 'D'
ALLOTMENT_SUPPLEMENT_COST_TYPE_BYPAXESDAYS = 'PD'
ALLOTMENT_SUPPLEMENT_COST_TYPES = (
    (ALLOTMENT_SUPPLEMENT_COST_TYPE_FIXED, 'Fixed'),
    (ALLOTMENT_SUPPLEMENT_COST_TYPE_BYPAXES, 'By Paxes'),
    (ALLOTMENT_SUPPLEMENT_COST_TYPE_BYDAYS, 'By Days'),
    (ALLOTMENT_SUPPLEMENT_COST_TYPE_BYPAXESDAYS, 'By Paxes Days'),
)

TRANSFER_SUPPLEMENT_COST_TYPE_FIXED = 'F'
TRANSFER_SUPPLEMENT_COST_TYPE_BYTRANSPORTS = 'T'
TRANSFER_SUPPLEMENT_COST_TYPE_BYHOURS = 'H'
TRANSFER_SUPPLEMENT_COST_TYPE_BYTRANSPORTSHOURS = 'TH'
TRANSFER_SUPPLEMENT_COST_TYPES = (
    (TRANSFER_SUPPLEMENT_COST_TYPE_FIXED, 'Fixed'),
    (TRANSFER_SUPPLEMENT_COST_TYPE_BYTRANSPORTS, 'By Transports'),
    (TRANSFER_SUPPLEMENT_COST_TYPE_BYHOURS, 'By Hours'),
    (TRANSFER_SUPPLEMENT_COST_TYPE_BYTRANSPORTSHOURS, 'By Transports Hours'),
)

BOARD_TYPE_NB = 'NB'
BOARD_TYPE_BB = 'BB'
BOARD_TYPE_HB = 'HB'
BOARD_TYPE_FB = 'FB'
BOARD_TYPE_AI = 'AI'
BOARD_TYPES = (
    (BOARD_TYPE_NB, 'NB'),
    (BOARD_TYPE_BB, 'BB'),
    (BOARD_TYPE_HB, 'HB'),
    (BOARD_TYPE_FB, 'FB'),
    (BOARD_TYPE_AI, 'AI'),
)
PAX_TYPE_BABY = 'B'
PAX_TYPE_CHILD = 'C'
PAX_TYPE_ADULT = 'A'
PAX_TYPE_SENIOR = 'S'
PAX_TYPES = (
    (PAX_TYPE_BABY, 'Baby'),
    (PAX_TYPE_CHILD, 'Child'),
    (PAX_TYPE_ADULT, 'Adult'),
    (PAX_TYPE_SENIOR, 'Senior'),
)
PAX_COMBO_A = 'A'
PAX_COMBO_AC = 'AC'
PAX_COMBO_AB = 'AB'
PAX_COMBO_ACC = 'ACC'
PAX_COMBO_ACB = 'ACB'
PAX_COMBO_ABB = 'ABB'
PAX_COMBO_AA = 'AA'
PAX_COMBO_AAC = 'AAC'
PAX_COMBO_AAB = 'AAB'
PAX_COMBO_AACC = 'AACC'
PAX_COMBO_AACB = 'AACB'
PAX_COMBO_AABB = 'AABB'
PAX_COMBO_AAA = 'AAA'
PAX_COMBO_AAAC = 'AAAC'
PAX_COMBO_AAAB = 'AAAB'
PAX_COMBO_AAACC = 'AAACC'
PAX_COMBO_AAACB = 'AAACB'
PAX_COMBO_AAABB = 'AAABB'
PAX_COMBO_AS = 'AS'
PAX_COMBO_ASC = 'ASC'
PAX_COMBO_ASB = 'ASB'
PAX_COMBO_ASCC = 'ASCC'
PAX_COMBO_ASCB = 'ASCB'
PAX_COMBO_ASBB = 'ASBB'
PAX_COMBO_ASS = 'ASS'
PAX_COMBO_ASSC = 'ASSC'
PAX_COMBO_ASSB = 'ASSB'
PAX_COMBO_ASSCC = 'ASSCC'
PAX_COMBO_ASSCB = 'ASSCB'
PAX_COMBO_ASSBB = 'ASSBB'
PAX_COMBO_AAS = 'AAS'
PAX_COMBO_AASC = 'AASC'
PAX_COMBO_AASB = 'AASB'
PAX_COMBO_AASCC = 'AASCC'
PAX_COMBO_AASCB = 'AASCB'
PAX_COMBO_AASBB = 'AASBB'
PAX_COMBO_S = 'S'
PAX_COMBO_SC = 'SC'
PAX_COMBO_SB = 'SB'
PAX_COMBO_SCC = 'SCC'
PAX_COMBO_SCB = 'SCB'
PAX_COMBO_SBB = 'SBB'
PAX_COMBO_SS = 'SS'
PAX_COMBO_SSC = 'SSC'
PAX_COMBO_SSB = 'SSB'
PAX_COMBO_SSCC = 'SSCC'
PAX_COMBO_SSCB = 'SSCB'
PAX_COMBO_SSBB = 'SSBB'
PAX_COMBO_SSS = 'SSS'
PAX_COMBO_SSSC = 'SSSC'
PAX_COMBO_SSSB = 'SSSB'
PAX_COMBO_SSSCC = 'SSSCC'
PAX_COMBO_SSSCB = 'SSSCB'
PAX_COMBO_SSSBB = 'SSSBB'
PAX_COMBOS = (
    (PAX_COMBO_A, '1A'),
    (PAX_COMBO_AC, '1A1C'),
    (PAX_COMBO_AB, '1A1B'),
    (PAX_COMBO_ACC, '1A2C'),
    (PAX_COMBO_ACB, '1A1C1B'),
    (PAX_COMBO_ABB, '1A2B'),
    (PAX_COMBO_AA, '2A'),
    (PAX_COMBO_AAC, '2A1C'),
    (PAX_COMBO_AAB, '2A1B'),
    (PAX_COMBO_AACC, '2A2C'),
    (PAX_COMBO_AACB, '2A1C1B'),
    (PAX_COMBO_AABB, '2A2B'),
    (PAX_COMBO_AAA, '3A'),
    (PAX_COMBO_AAAC, '3A1C'),
    (PAX_COMBO_AAAB, '3A1B'),
    (PAX_COMBO_AAACC, '3A2C'),
    (PAX_COMBO_AAACB, '3A1C1B'),
    (PAX_COMBO_AAABB, '3A2B'),
    (PAX_COMBO_AS, '1A1S'),
    (PAX_COMBO_ASC, '1A1S1C'),
    (PAX_COMBO_ASB, '1A1S1B'),
    (PAX_COMBO_ASCC, '1A1S2C'),
    (PAX_COMBO_ASCB, '1A1S1C1B'),
    (PAX_COMBO_ASBB, '1A1S2B'),
    (PAX_COMBO_ASS, '1A2S'),
    (PAX_COMBO_ASSC, '1A2S1C'),
    (PAX_COMBO_ASSB, '1A2S1B'),
    (PAX_COMBO_ASSCC, '1A2S2C'),
    (PAX_COMBO_ASSCB, '1A2S1C1B'),
    (PAX_COMBO_ASSBB, '1A2S2B'),
    (PAX_COMBO_AAS, '2A1S'),
    (PAX_COMBO_AASC, '2A1S1C'),
    (PAX_COMBO_AASB, '2A1S1B'),
    (PAX_COMBO_AASCC, '2A1S2C'),
    (PAX_COMBO_AASCB, '2A1S1C1B'),
    (PAX_COMBO_AASBB, '2A1S2B'),
    (PAX_COMBO_S, '1S'),
    (PAX_COMBO_SC, '1S1C'),
    (PAX_COMBO_SB, '1S1B'),
    (PAX_COMBO_SCC, '1S2C'),
    (PAX_COMBO_SCB, '1S1C1B'),
    (PAX_COMBO_SBB, '1S2B'),
    (PAX_COMBO_SS, '2S'),
    (PAX_COMBO_SSC, '2S1C'),
    (PAX_COMBO_SSB, '2S1B'),
    (PAX_COMBO_SSCC, '2S2C'),
    (PAX_COMBO_SSCB, '2S1C1B'),
    (PAX_COMBO_SSBB, '2S2B'),
    (PAX_COMBO_SSS, '3S'),
    (PAX_COMBO_SSSC, '3S1C'),
    (PAX_COMBO_SSSB, '3S1B'),
    (PAX_COMBO_SSSCC, '3S2C'),
    (PAX_COMBO_SSSCB, '3S1C1B'),
    (PAX_COMBO_SSSBB, '3S2B'),
)
