test_data_1gen = {
    "id": 4073,
    "label": None,
    "task": "Prediction",
    "biotransformer_option": "CYP450",
    "number_of_steps": 1,
    "status": "Done",
    "number_of_starting_compounds": 1,
    "total_prediction_time_in_ms": 2424.04,
    "invalid_compounds": [
      
    ],
    "predictions": [
      {
        "identifier": "Q4073-1",
        "starting_compound": "CC(=O)NC1=CC=C(O)C=C1",
        "status": "Done",
        "nr_of_biotransformations": 6,
        "biotransformations": [
          {
            "biosystem": "Human",
            "reaction_type": "N-hydroxylation of secondary arylamide",
            "metabolic_enzymes": [
              "CYP1A2"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1",
                "inchikey": "RZVAJINKPMORJF-UHFFFAOYSA-N",
                "title": "acetaminophen",
                "pubchem_cid": "1983"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N(C1=CC=C(O)C=C1)O",
                "inchikey": "CCYHKRWGLAJQTB-UHFFFAOYSA-N",
                "title": "N-Hydroxyparacetamol",
                "pubchem_cid": "45750"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Hydroxylation of benzene on carbon orhto to a strongly electron donating group",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2E1",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1",
                "inchikey": "RZVAJINKPMORJF-UHFFFAOYSA-N",
                "title": "acetaminophen",
                "pubchem_cid": "1983"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1O",
                "inchikey": "LMFGGAOMLJLKJJ-UHFFFAOYSA-N",
                "title": "Acetamide, N-(2,4-dihydroxyphenyl)-",
                "pubchem_cid": "580765"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Oxidation of p-substituted anilides",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C9",
              "CYP2D6",
              "CYP2E1",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1",
                "inchikey": "RZVAJINKPMORJF-UHFFFAOYSA-N",
                "title": "acetaminophen",
                "pubchem_cid": "1983"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N=C1C=CC(=O)C=C1",
                "inchikey": "URNSECGXFRDEDC-UHFFFAOYSA-N",
                "title": "Napqi",
                "pubchem_cid": "39763"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "o-Hydroxylation of phenol",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2D6",
              "CYP2E1",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1",
                "inchikey": "RZVAJINKPMORJF-UHFFFAOYSA-N",
                "title": "acetaminophen",
                "pubchem_cid": "1983"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C(=C1)O",
                "inchikey": "IPFBMHOMTSBTSU-UHFFFAOYSA-N",
                "title": "3-Hydroxyacetaminophen",
                "pubchem_cid": "161950"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Alpha hydroxylation of carbonyl group",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2D6",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1",
                "inchikey": "RZVAJINKPMORJF-UHFFFAOYSA-N",
                "title": "acetaminophen",
                "pubchem_cid": "1983"
              }
            ],
            "products": [
              {
                "smiles": "C(C(=O)NC1=CC=C(O)C=C1)O",
                "inchikey": "AFOASBUSAJOWLT-UHFFFAOYSA-N",
                "title": "AKOS022194070",
                "pubchem_cid": "12748683"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "N-hydroxylation of anilide",
            "metabolic_enzymes": [
              "CYP2E1"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1",
                "inchikey": "RZVAJINKPMORJF-UHFFFAOYSA-N",
                "title": "acetaminophen",
                "pubchem_cid": "1983"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N(C1=CC=C(O)C=C1)O",
                "inchikey": "CCYHKRWGLAJQTB-UHFFFAOYSA-N",
                "title": "N-Hydroxyparacetamol",
                "pubchem_cid": "45750"
              }
            ]
          }
        ]
      }
    ],
    "number_of_unique_metabolites": 5,
    "prediction_errors": None
  }







test_data_2gen = {
    "id": 4101,
    "label": None,
    "task": "Prediction",
    "biotransformer_option": "CYP450",
    "number_of_steps": 2,
    "status": "Done",
    "number_of_starting_compounds": 1,
    "total_prediction_time_in_ms": 5569.98,
    "invalid_compounds": [
      
    ],
    "predictions": [
      {
        "identifier": "Q4101-1",
        "starting_compound": "CC(=O)NC1=CC=C(O)C=C1",
        "status": "Done",
        "nr_of_biotransformations": 24,
        "biotransformations": [
          {
            "biosystem": "Human",
            "reaction_type": "N-hydroxylation of secondary arylamide",
            "metabolic_enzymes": [
              "CYP1A2"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1",
                "inchikey": "RZVAJINKPMORJF-UHFFFAOYSA-N",
                "title": "acetaminophen",
                "pubchem_cid": "1983"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N(C1=CC=C(O)C=C1)O",
                "inchikey": "CCYHKRWGLAJQTB-UHFFFAOYSA-N",
                "title": "N-Hydroxyparacetamol",
                "pubchem_cid": "45750"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Hydroxylation of benzene on carbon orhto to a strongly electron donating group",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2E1",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1",
                "inchikey": "RZVAJINKPMORJF-UHFFFAOYSA-N",
                "title": "acetaminophen",
                "pubchem_cid": "1983"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1O",
                "inchikey": "LMFGGAOMLJLKJJ-UHFFFAOYSA-N",
                "title": "Acetamide, N-(2,4-dihydroxyphenyl)-",
                "pubchem_cid": "580765"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Oxidation of p-substituted anilides",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C9",
              "CYP2D6",
              "CYP2E1",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1",
                "inchikey": "RZVAJINKPMORJF-UHFFFAOYSA-N",
                "title": "acetaminophen",
                "pubchem_cid": "1983"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N=C1C=CC(=O)C=C1",
                "inchikey": "URNSECGXFRDEDC-UHFFFAOYSA-N",
                "title": "Napqi",
                "pubchem_cid": "39763"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "o-Hydroxylation of phenol",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2D6",
              "CYP2E1",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1",
                "inchikey": "RZVAJINKPMORJF-UHFFFAOYSA-N",
                "title": "acetaminophen",
                "pubchem_cid": "1983"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C(=C1)O",
                "inchikey": "IPFBMHOMTSBTSU-UHFFFAOYSA-N",
                "title": "3-Hydroxyacetaminophen",
                "pubchem_cid": "161950"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Alpha hydroxylation of carbonyl group",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2D6",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1",
                "inchikey": "RZVAJINKPMORJF-UHFFFAOYSA-N",
                "title": "acetaminophen",
                "pubchem_cid": "1983"
              }
            ],
            "products": [
              {
                "smiles": "C(C(=O)NC1=CC=C(O)C=C1)O",
                "inchikey": "AFOASBUSAJOWLT-UHFFFAOYSA-N",
                "title": "AKOS022194070",
                "pubchem_cid": "12748683"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "N-hydroxylation of anilide",
            "metabolic_enzymes": [
              "CYP2E1"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1",
                "inchikey": "RZVAJINKPMORJF-UHFFFAOYSA-N",
                "title": "acetaminophen",
                "pubchem_cid": "1983"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N(C1=CC=C(O)C=C1)O",
                "inchikey": "CCYHKRWGLAJQTB-UHFFFAOYSA-N",
                "title": "N-Hydroxyparacetamol",
                "pubchem_cid": "45750"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "o-Hydroxylation of phenol",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2D6",
              "CYP2E1",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)N(C1=CC=C(O)C=C1)O",
                "inchikey": "CCYHKRWGLAJQTB-UHFFFAOYSA-N",
                "title": "N-Hydroxyparacetamol",
                "pubchem_cid": "45750"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N(C1=CC=C(O)C(=C1)O)O",
                "inchikey": "GFURKNGBWGIJNW-UHFFFAOYSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Alpha hydroxylation of carbonyl group",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2D6",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)N(C1=CC=C(O)C=C1)O",
                "inchikey": "CCYHKRWGLAJQTB-UHFFFAOYSA-N",
                "title": "N-Hydroxyparacetamol",
                "pubchem_cid": "45750"
              }
            ],
            "products": [
              {
                "smiles": "C(C(=O)N(C1=CC=C(O)C=C1)O)O",
                "inchikey": "JRIOLBAXVNDJCR-UHFFFAOYSA-N",
                "title": "dihydroxy paracetamol",
                "pubchem_cid": "138392250"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "N-hydroxylation of secondary arylamide",
            "metabolic_enzymes": [
              "CYP1A2"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1O",
                "inchikey": "LMFGGAOMLJLKJJ-UHFFFAOYSA-N",
                "title": "Acetamide, N-(2,4-dihydroxyphenyl)-",
                "pubchem_cid": "580765"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N(C1=CC=C(O)C=C1O)O",
                "inchikey": "TVLUGOLKPYCLGT-UHFFFAOYSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Hydroxylation of benzene on carbon orhto to a strongly electron donating group",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2E1",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1O",
                "inchikey": "LMFGGAOMLJLKJJ-UHFFFAOYSA-N",
                "title": "Acetamide, N-(2,4-dihydroxyphenyl)-",
                "pubchem_cid": "580765"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)NC1=C(C=C(O)C=C1O)O",
                "inchikey": "YJICPOAYWGLWQJ-UHFFFAOYSA-N",
                "title": "SCHEMBL2485690",
                "pubchem_cid": "67425644"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Oxidation of p-substituted anilides",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C9",
              "CYP2D6",
              "CYP2E1",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1O",
                "inchikey": "LMFGGAOMLJLKJJ-UHFFFAOYSA-N",
                "title": "Acetamide, N-(2,4-dihydroxyphenyl)-",
                "pubchem_cid": "580765"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N=C1C=CC(=O)C=C1O",
                "inchikey": "OZXQBDAZUYEYCG-VQHVLOKHSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Alpha hydroxylation of carbonyl group",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2D6",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1O",
                "inchikey": "LMFGGAOMLJLKJJ-UHFFFAOYSA-N",
                "title": "Acetamide, N-(2,4-dihydroxyphenyl)-",
                "pubchem_cid": "580765"
              }
            ],
            "products": [
              {
                "smiles": "C(C(=O)NC1=CC=C(O)C=C1O)O",
                "inchikey": "WMCWDNFIRKSTGV-UHFFFAOYSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "N-hydroxylation of anilide",
            "metabolic_enzymes": [
              "CYP2E1"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C=C1O",
                "inchikey": "LMFGGAOMLJLKJJ-UHFFFAOYSA-N",
                "title": "Acetamide, N-(2,4-dihydroxyphenyl)-",
                "pubchem_cid": "580765"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N(C1=CC=C(O)C=C1O)O",
                "inchikey": "TVLUGOLKPYCLGT-UHFFFAOYSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Epxodation of alkene",
            "metabolic_enzymes": [
              "CYP2E1"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)N=C1C=CC(=O)C=C1",
                "inchikey": "URNSECGXFRDEDC-UHFFFAOYSA-N",
                "title": "Napqi",
                "pubchem_cid": "39763"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N=C1C=CC(=O)C2C1O2",
                "inchikey": "OJIPGYWMSLSWLO-WEVVVXLNSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "N-hydroxylation of secondary arylamide",
            "metabolic_enzymes": [
              "CYP1A2"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C(=C1)O",
                "inchikey": "IPFBMHOMTSBTSU-UHFFFAOYSA-N",
                "title": "3-Hydroxyacetaminophen",
                "pubchem_cid": "161950"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N(C1=CC=C(O)C(=C1)O)O",
                "inchikey": "GFURKNGBWGIJNW-UHFFFAOYSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Hydroxylation of benzene on carbon orhto to a strongly electron donating group",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2E1",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C(=C1)O",
                "inchikey": "IPFBMHOMTSBTSU-UHFFFAOYSA-N",
                "title": "3-Hydroxyacetaminophen",
                "pubchem_cid": "161950"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)NC1=C(C=C(O)C(=C1)O)O",
                "inchikey": "WHAFZYSCLHLURY-UHFFFAOYSA-N",
                "title": "N-(2,4,5-trihydroxyphenyl)acetamide",
                "pubchem_cid": "129853780"
              },
              {
                "smiles": "CC(=O)NC1=CC=C(O)C(=C1O)O",
                "inchikey": "LPDJZWRLGINFNA-UHFFFAOYSA-N",
                "title": "SCHEMBL6783926",
                "pubchem_cid": "10154334"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Oxidation of p-substituted anilides",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C9",
              "CYP2D6",
              "CYP2E1",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C(=C1)O",
                "inchikey": "IPFBMHOMTSBTSU-UHFFFAOYSA-N",
                "title": "3-Hydroxyacetaminophen",
                "pubchem_cid": "161950"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N=C1C=CC(=O)C(=C1)O",
                "inchikey": "USBICVFIVFRDOT-RMKNXTFCSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Alpha hydroxylation of carbonyl group",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2A6",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2D6",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C(=C1)O",
                "inchikey": "IPFBMHOMTSBTSU-UHFFFAOYSA-N",
                "title": "3-Hydroxyacetaminophen",
                "pubchem_cid": "161950"
              }
            ],
            "products": [
              {
                "smiles": "C(C(=O)NC1=CC=C(O)C(=C1)O)O",
                "inchikey": "ZCAWRIWBJPFJHI-UHFFFAOYSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "N-hydroxylation of anilide",
            "metabolic_enzymes": [
              "CYP2E1"
            ],
            "substrates": [
              {
                "smiles": "CC(=O)NC1=CC=C(O)C(=C1)O",
                "inchikey": "IPFBMHOMTSBTSU-UHFFFAOYSA-N",
                "title": "3-Hydroxyacetaminophen",
                "pubchem_cid": "161950"
              }
            ],
            "products": [
              {
                "smiles": "CC(=O)N(C1=CC=C(O)C(=C1)O)O",
                "inchikey": "GFURKNGBWGIJNW-UHFFFAOYSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "N-hydroxylation of secondary arylamide",
            "metabolic_enzymes": [
              "CYP1A2"
            ],
            "substrates": [
              {
                "smiles": "C(C(=O)NC1=CC=C(O)C=C1)O",
                "inchikey": "AFOASBUSAJOWLT-UHFFFAOYSA-N",
                "title": "AKOS022194070",
                "pubchem_cid": "12748683"
              }
            ],
            "products": [
              {
                "smiles": "C(C(=O)N(C1=CC=C(O)C=C1)O)O",
                "inchikey": "JRIOLBAXVNDJCR-UHFFFAOYSA-N",
                "title": "dihydroxy paracetamol",
                "pubchem_cid": "138392250"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Hydroxylation of benzene on carbon orhto to a strongly electron donating group",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "C(C(=O)NC1=CC=C(O)C=C1)O",
                "inchikey": "AFOASBUSAJOWLT-UHFFFAOYSA-N",
                "title": "AKOS022194070",
                "pubchem_cid": "12748683"
              }
            ],
            "products": [
              {
                "smiles": "C(C(=O)NC1=CC=C(O)C=C1O)O",
                "inchikey": "WMCWDNFIRKSTGV-UHFFFAOYSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Oxidation of p-substituted anilides",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2C9",
              "CYP2D6",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "C(C(=O)NC1=CC=C(O)C=C1)O",
                "inchikey": "AFOASBUSAJOWLT-UHFFFAOYSA-N",
                "title": "AKOS022194070",
                "pubchem_cid": "12748683"
              }
            ],
            "products": [
              {
                "smiles": "C(C(=O)N=C1C=CC(=O)C=C1)O",
                "inchikey": "FZHJUUNZXDLSKL-UHFFFAOYSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "Oxidation of primary alcohol to aldehyde",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "C(C(=O)NC1=CC=C(O)C=C1)O",
                "inchikey": "AFOASBUSAJOWLT-UHFFFAOYSA-N",
                "title": "AKOS022194070",
                "pubchem_cid": "12748683"
              }
            ],
            "products": [
              {
                "smiles": "C(C(=O)NC1=CC=C(O)C=C1)=O",
                "inchikey": "AIPJRWVZJJIQTR-UHFFFAOYSA-N",
                "title": "SCHEMBL3708912",
                "pubchem_cid": "22743962"
              }
            ]
          },
          {
            "biosystem": "Human",
            "reaction_type": "o-Hydroxylation of phenol",
            "metabolic_enzymes": [
              "CYP1A2",
              "CYP2C8",
              "CYP2C9",
              "CYP2C19",
              "CYP2D6",
              "CYP3A4"
            ],
            "substrates": [
              {
                "smiles": "C(C(=O)NC1=CC=C(O)C=C1)O",
                "inchikey": "AFOASBUSAJOWLT-UHFFFAOYSA-N",
                "title": "AKOS022194070",
                "pubchem_cid": "12748683"
              }
            ],
            "products": [
              {
                "smiles": "C(C(=O)NC1=CC=C(O)C(=C1)O)O",
                "inchikey": "ZCAWRIWBJPFJHI-UHFFFAOYSA-N",
                "title": None,
                "pubchem_cid": None
              }
            ]
          }
        ]
      }
    ],
    "number_of_unique_metabolites": 18,
    "prediction_errors": None
  }