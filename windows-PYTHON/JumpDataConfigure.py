# -*- coding: utf-8 -*-

class DataConfigure(object):
  def __init__(self):
      self.initParameters();
      
  def initParameters(self):
      
      self.PeriodTimeOrder = 0;
      
      self.RealAngOrder = 0;
      self.RefAngOrder = 1;
      self.RefVelOrder = 2;
      self.RealEncOrder = 3;
      self.RefEncOrder = 4;
      self.RealVelOrder = 5;
      self.RealCurrentOrder = 7;
      self.RefCurrentOrder = 8;
      self.RefTauOrder = 9;
      
      self.RHip1Order = 1;
      self.RHip2Order = 12;
      self.RHip3Order = 23;
      self.RKneeOrder = 34;
      self.RAnkle5Order = 45;
      self.RAnkle6Order = 56;
      self.LHip1Order = 67;
      self.LHip2Order = 78;
      self.LHip3Order = 89;
      self.LKneeOrder = 100;
      self.LAnkle5Order = 111;
      self.LAnkle6Order = 122;
      self.RArmOrder = 133;
      self.LArmOrder = 144;
            
      self.TorsoRollActOrder = 155;
      self.TorsoPitchActOrder = 156;
      self.TorsoRollVActOrder = 161;
      self.TorsoPitchVActOrder = 162;
      self.TorsoXAActOrder = 158;
      self.TorsoYAActOrder = 159;
      self.TorsoZAActOrder = 160;
      
      self.RlegForceActX = 164;
      self.RlegForceActY = 165;
      self.RlegForceActZ = 166;
      self.RlegTorqueActX = 167;
      self.RlegTorqueActY = 168;
      self.RlegTorqueActZ = 169;
 
      self.LlegForceActX = 170;
      self.LlegForceActY = 171;
      self.LlegForceActZ = 172;
      self.LlegTorqueActX = 173;
      self.LlegTorqueActY = 174;
      self.LlegTorqueActZ = 175;
      
      self.ComActX = 192;
      self.ComActY = 193;
      self.ComActZ = 194;
      self.ComRefX = 201;
      self.ComRefY = 202;
      self.ComRefZ = 203;
      
      self.ddx = 195;
      self.ddz = 196;
      self.ZmpRefX = 197;
      self.RZmpRefX = 199;
      self.LZmpRefX = 200;
      
      self.AmomY = 198;
            
      # self.RlegForceRefX = 112;
      # self.RlegForceRefY = 113;
      # self.RlegForceRefZ = 114;
 
      # self.LlegForceRefX = 115;
      # self.LlegForceRefY = 116;
      # self.LlegForceRefZ = 117;
      
      # self.StateEstimX = 126;
      # self.StateEstimY = 127;
      # self.StateEstimZ = 128;
      # self.StateEstimRoll = 126;
      # self.StateEstimPitch = 127;
      # self.StateEstimYaw = 128;
      
      # self.StateEstimVX = 129;
      # self.StateEstimVY = 130;
      # self.StateEstimVZ = 131;
      
      # self.StateEstimWX_b = 129;
      # self.StateEstimWY_b = 130;
      # self.StateEstimWZ_b = 131;
      
      # self.StateEstimWX_b = 129;
      # self.StateEstimWY_b = 130;
      # self.StateEstimWZ_b = 131;