# Example of dmin classifier

from clf_utils import loadData, defineClassifier, trainClassifier, testClassifier, PrintConfusion, PlotFeatures, PlotDecisionLines

(X,d,Xt,dt) = loadData('G2')                              # load training and testing data
name        = 'NearestCentroid'                           # name of the classifier
params      = ''                                          # parameters of the classifier
clf         = defineClassifier([name,params])             # classifier definition
clf         = trainClassifier(clf,X,d)                    # classifier training
ds          = testClassifier(clf,Xt)                      # classifier testing
PrintConfusion(dt,ds)                                     # confusion matrix
PlotDecisionLines(clf,X)                                  # decision lines
PlotFeatures(X,d,'dmin')                                  # feature space