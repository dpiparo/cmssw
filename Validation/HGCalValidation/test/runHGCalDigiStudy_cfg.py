import FWCore.ParameterSet.Config as cms

#from Configuration.Eras.Era_Phase2C4_timing_layer_bar_cff import Phase2C4_timing_layer_bar
#process = cms.Process('PROD',Phase2C4_timing_layer_bar)
#process.load('Configuration.Geometry.GeometryExtended2026D35_cff')
#process.load('Configuration.Geometry.GeometryExtended2026D35Reco_cff')

from Configuration.Eras.Era_Phase2C8_timing_layer_bar_cff import Phase2C8_timing_layer_bar
process = cms.Process('PROD',Phase2C8_timing_layer_bar)
process.load('Configuration.Geometry.GeometryExtended2026D41_cff')
process.load('Configuration.Geometry.GeometryExtended2026D41Reco_cff')

#from Configuration.Eras.Era_Phase2C9_timing_layer_bar_cff import Phase2C9_timing_layer_bar
#process = cms.Process('PROD',Phase2C9_timing_layer_bar)
#process.load('Configuration.Geometry.GeometryExtended2026D46_cff')
#process.load('Configuration.Geometry.GeometryExtended2026D46Reco_cff')

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Validation.HGCalValidation.hgcDigiStudy_cfi')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag.globaltag = autoCond['phase2_realistic']

#if hasattr(process,'MessageLogger'):
#    process.MessageLogger.categories.append('HGCalValidation')

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        'file:step2_29034.root',
#       'root://cms-xrd-global.cern.ch//store/relval/CMSSW_9_1_1_patch1/RelValSingleElectronPt35Extended/GEN-SIM-RECO/91X_upgrade2023_realistic_v1_D17-v1/10000/10D95AC2-B14A-E711-BC4A-0CC47A7C3638.root',
        )
                            )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('hgcDigiD41tt.root'),
                                   closeFileFast = cms.untracked.bool(True)
                                   )

process.raw2digi_step = cms.Path(process.RawToDigi)
process.analysis_step = cms.Path(process.hgcalDigiStudyEE+
                                 process.hgcalDigiStudyHEF+
                                 process.hgcalDigiStudyHEB)
process.hgcalDigiStudyEE.verbosity = 1
process.hgcalDigiStudyHEF.verbosity = 1
process.hgcalDigiStudyHEB.verbosity = 1

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.analysis_step)
