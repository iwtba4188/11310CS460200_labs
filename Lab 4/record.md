loss_function = "cross_entropy"
layers_dims = [784, 8, 16, 8, num_classes]
activation_fn = ["relu", "relu", "relu", "softmax"]
learning_rate = 1e-2
num_iterations = 1000
print_loss = True
print_freq = 50
decrease_freq = 100
decrease_proportion = 0.98
batch_size = 128
>>
Loss after iteration 0: 1.3818798562062202
Loss after iteration 50: 1.066289189155029
Loss after iteration 100: 0.9849869514352063
Loss after iteration 150: 0.9283953836748305
Loss after iteration 200: 0.8951153175296824
Loss after iteration 250: 0.8696343977130874
Loss after iteration 300: 0.8576503260549301
Loss after iteration 350: 0.8428077495345453
Loss after iteration 400: 0.828065031632089
Loss after iteration 450: 0.820031331742923
Loss after iteration 500: 0.8112894407798178
Loss after iteration 550: 0.8039587240197335
Loss after iteration 600: 0.7996378601332861
Loss after iteration 650: 0.7961664497276946
Loss after iteration 700: 0.7897351240618111
Loss after iteration 750: 0.7806107404349532
Loss after iteration 800: 0.7796941373422374
Loss after iteration 850: 0.7759740398523464
Loss after iteration 900: 0.7721763256314758
Loss after iteration 950: 0.7656048778949991
>>
training------
Accuracy: 68.95%
f1 score for each class: [0.74947946 0.80356083 0.45740508 0.69124218]
f1_macro score: 0.68
validation------
Accuracy: 64.99%
f1 score for each class: [0.72546359 0.7710084  0.40053405 0.63744198]
f1_macro score: 0.63
>>
# 0.47911
======================================================
loss_function = "cross_entropy"
layers_dims = [784, 32, 64, 64, num_classes]
activation_fn = ["relu", "relu", "relu", "softmax"]
learning_rate = 1e-2
num_iterations = 1000
print_loss = True
print_freq = 50
decrease_freq = 100
decrease_proportion = 0.98
batch_size = 128
>>
Loss after iteration 0: 1.3812600129883066
Loss after iteration 50: 0.9561729160836208
Loss after iteration 100: 0.7544081161335169
Loss after iteration 150: 0.6473723143497152
Loss after iteration 200: 0.586561024312456
Loss after iteration 250: 0.5365797555423937
Loss after iteration 300: 0.4970432575604351
Loss after iteration 350: 0.46467857741202157
Loss after iteration 400: 0.43676787890071583
Loss after iteration 450: 0.4196816471759817
Loss after iteration 500: 0.38925926390432314
Loss after iteration 550: 0.3681023772966325
Loss after iteration 600: 0.35221900566710335
Loss after iteration 650: 0.3508543834581593
Loss after iteration 700: 0.3384616935196207
Loss after iteration 750: 0.31184582458869115
Loss after iteration 800: 0.29924237847653384
Loss after iteration 850: 0.2800426500437891
Loss after iteration 900: 0.27900318946320374
Loss after iteration 950: 0.2572463432812669
>>
training------
Accuracy: 89.80%
f1 score for each class: [0.94047555 0.94686612 0.78361153 0.88744197]
f1_macro score: 0.89
validation------
Accuracy: 78.81%
f1 score for each class: [0.85562016 0.85462146 0.61215933 0.77205882]
f1_macro score: 0.77
>>
# 0.52209
======================================================
loss_function = "cross_entropy"
layers_dims = [784, 32, num_classes]
activation_fn = ["relu", "softmax"]
learning_rate = 1e-2
num_iterations = 1500
print_loss = True
print_freq = 20
decrease_freq = 100
decrease_proportion = 0.9
batch_size = 64
>>
Loss after iteration 0: 1.3626722273152907
Loss after iteration 20: 1.094318545890931
Loss after iteration 40: 0.97988546914606
Loss after iteration 60: 0.8991551801776485
Loss after iteration 80: 0.8438016218624443
Loss after iteration 100: 0.800652214312249
Loss after iteration 120: 0.7692880785771012
Loss after iteration 140: 0.7448661068242133
Loss after iteration 160: 0.7236072314079728
Loss after iteration 180: 0.7058656346286067
Loss after iteration 200: 0.6891445095463615
Loss after iteration 220: 0.6739740712659401
Loss after iteration 240: 0.6624901516640337
Loss after iteration 260: 0.6470690596004194
Loss after iteration 280: 0.6393736971059478
Loss after iteration 300: 0.6293914294694624
Loss after iteration 320: 0.6169843953939678
Loss after iteration 340: 0.609725719275307
Loss after iteration 360: 0.6027425067635619
Loss after iteration 380: 0.5959664402535603
Loss after iteration 400: 0.5879802983757543
Loss after iteration 420: 0.5803881173144102
Loss after iteration 440: 0.5752869291211293
Loss after iteration 460: 0.5681325735178783
Loss after iteration 480: 0.5648186748007072
Loss after iteration 500: 0.5594741378595716
Loss after iteration 520: 0.5521902646663353
Loss after iteration 540: 0.5468721815442914
Loss after iteration 560: 0.5442640300372479
Loss after iteration 580: 0.5405179452448153
Loss after iteration 600: 0.5369441663404039
Loss after iteration 620: 0.52899574992226
Loss after iteration 640: 0.5279235404870951
Loss after iteration 660: 0.5230683142337818
Loss after iteration 680: 0.5212501017695395
Loss after iteration 700: 0.5179216184604953
Loss after iteration 720: 0.5132553344508664
Loss after iteration 740: 0.5105647432569349
Loss after iteration 760: 0.5074283497592775
Loss after iteration 780: 0.5048266639540263
Loss after iteration 800: 0.5026424393541937
Loss after iteration 820: 0.4984783414644774
Loss after iteration 840: 0.496031861177309
Loss after iteration 860: 0.4949748489025453
Loss after iteration 880: 0.49193663754864364
Loss after iteration 900: 0.48933125299856206
Loss after iteration 920: 0.48719352084856254
Loss after iteration 940: 0.4841694958778954
Loss after iteration 960: 0.48381715966898675
Loss after iteration 980: 0.4816586245715213
Loss after iteration 1000: 0.47978246064428526
Loss after iteration 1020: 0.4764261265311091
Loss after iteration 1040: 0.4751686167246464
Loss after iteration 1060: 0.4745135891808292
Loss after iteration 1080: 0.4715857769325906
Loss after iteration 1100: 0.47030752067942366
Loss after iteration 1120: 0.46716315309782563
Loss after iteration 1140: 0.46748796311533264
Loss after iteration 1160: 0.46507037101058635
Loss after iteration 1180: 0.4646727589067835
Loss after iteration 1200: 0.46257787998834077
Loss after iteration 1220: 0.46104928103589354
Loss after iteration 1240: 0.45976848705855516
Loss after iteration 1260: 0.4582549853732216
Loss after iteration 1280: 0.457329060810067
Loss after iteration 1300: 0.4567799427262926
Loss after iteration 1320: 0.4550255463166273
Loss after iteration 1340: 0.45244346774085553
Loss after iteration 1360: 0.45273231730474855
Loss after iteration 1380: 0.45187753813065273
Loss after iteration 1400: 0.4497420485345073
Loss after iteration 1420: 0.4493639608457115
Loss after iteration 1440: 0.4479537155542982
Loss after iteration 1460: 0.4471453624195425
Loss after iteration 1480: 0.4463373124837156
>>
training------
Accuracy: 83.95%
f1 score for each class: [0.89022222 0.91994145 0.68268875 0.82748648]
f1_macro score: 0.83
validation------
Accuracy: 74.52%
f1 score for each class: [0.80616302 0.8444666  0.52459016 0.74589372]
f1_macro score: 0.73
>>
# 0.50890
======================================================
loss_function = "cross_entropy"
layers_dims = [784, 64, 32, num_classes]
activation_fn = ["relu", "relu", "softmax"]
learning_rate = 5e-3
num_iterations = 2000
print_loss = True
print_freq = 20
decrease_freq = 200
decrease_proportion = 0.8
batch_size = 64
>>
Loss after iteration 0: 1.3808193280062833
Loss after iteration 20: 1.1109244340717757
Loss after iteration 40: 0.9423414963113027
Loss after iteration 60: 0.8317282611005795
Loss after iteration 80: 0.75577558701788
Loss after iteration 100: 0.6994152739193387
Loss after iteration 120: 0.6605662327314608
Loss after iteration 140: 0.6234271903869777
Loss after iteration 160: 0.5891042133205858
Loss after iteration 180: 0.5705794477886127
Loss after iteration 200: 0.5436464533490721
Loss after iteration 220: 0.5054210334485018
Loss after iteration 240: 0.4948279600119834
Loss after iteration 260: 0.48406450603425244
Loss after iteration 280: 0.47040743747046126
Loss after iteration 300: 0.4581486024236447
Loss after iteration 320: 0.44541289204553214
Loss after iteration 340: 0.4403473913945771
Loss after iteration 360: 0.42319359242207094
Loss after iteration 380: 0.419448687552159
Loss after iteration 400: 0.4074884761737951
Loss after iteration 420: 0.38065867177506624
Loss after iteration 440: 0.3783763114113584
Loss after iteration 460: 0.36522221952873013
Loss after iteration 480: 0.3608623944234175
Loss after iteration 500: 0.3572104848805274
Loss after iteration 520: 0.35366758730956366
Loss after iteration 540: 0.3453655218752292
Loss after iteration 560: 0.34119030174550946
Loss after iteration 580: 0.334810508731828
Loss after iteration 600: 0.3302221866254643
Loss after iteration 620: 0.3105446903961644
Loss after iteration 640: 0.3043061408020995
Loss after iteration 660: 0.3019274229956198
Loss after iteration 680: 0.30043260026135155
Loss after iteration 700: 0.29050280759468716
Loss after iteration 720: 0.2892846915862248
Loss after iteration 740: 0.28679717585720094
Loss after iteration 760: 0.28308937632205744
Loss after iteration 780: 0.2806876117845666
Loss after iteration 800: 0.2747030845572942
Loss after iteration 820: 0.2595383216324093
Loss after iteration 840: 0.25664813624877997
Loss after iteration 860: 0.25419293995918557
Loss after iteration 880: 0.2527664801269945
Loss after iteration 900: 0.2502341166312758
Loss after iteration 920: 0.24783704110685173
Loss after iteration 940: 0.24367693889720296
Loss after iteration 960: 0.2439718090771762
Loss after iteration 980: 0.24092586453895487
Loss after iteration 1000: 0.23781229690701533
Loss after iteration 1020: 0.22477374821653623
Loss after iteration 1040: 0.22495733060975276
Loss after iteration 1060: 0.22149708824509734
Loss after iteration 1080: 0.21985076371474396
Loss after iteration 1100: 0.21685888347719431
Loss after iteration 1120: 0.21497879226574992
Loss after iteration 1140: 0.21399537716370953
Loss after iteration 1160: 0.21294854663154084
Loss after iteration 1180: 0.20845909404899313
Loss after iteration 1200: 0.20610739744921
Loss after iteration 1220: 0.19862637640973954
Loss after iteration 1240: 0.19884568439599987
Loss after iteration 1260: 0.19664939787408117
Loss after iteration 1280: 0.19429927130481986
Loss after iteration 1300: 0.19287531733222973
Loss after iteration 1320: 0.1913570408272412
Loss after iteration 1340: 0.19095983332531338
Loss after iteration 1360: 0.18852726935021324
Loss after iteration 1380: 0.18749211108644004
Loss after iteration 1400: 0.186245691136763
Loss after iteration 1420: 0.17921716896168383
Loss after iteration 1440: 0.1791723193842435
Loss after iteration 1460: 0.17864784568077954
Loss after iteration 1480: 0.17606033808668373
Loss after iteration 1500: 0.175571758626061
Loss after iteration 1520: 0.1738703164394363
Loss after iteration 1540: 0.17222036183243772
Loss after iteration 1560: 0.17275742774705244
Loss after iteration 1580: 0.1703378212701966
Loss after iteration 1600: 0.16947236713601724
Loss after iteration 1620: 0.16498996257503007
Loss after iteration 1640: 0.16472002982811526
Loss after iteration 1660: 0.16289986295472075
Loss after iteration 1680: 0.1620611434596919
Loss after iteration 1700: 0.16111786421754656
Loss after iteration 1720: 0.16023495598200985
Loss after iteration 1740: 0.15953044211498546
Loss after iteration 1760: 0.15828526309259972
Loss after iteration 1780: 0.1573916013807724
Loss after iteration 1800: 0.15571066565438274
Loss after iteration 1820: 0.15339443246072296
Loss after iteration 1840: 0.15245497935902283
Loss after iteration 1860: 0.15136708989512052
Loss after iteration 1880: 0.15130192442548537
Loss after iteration 1900: 0.15058666892428124
Loss after iteration 1920: 0.15016497767162798
Loss after iteration 1940: 0.14886467510726067
Loss after iteration 1960: 0.14880133060090397
Loss after iteration 1980: 0.1477827345814735
>>
training------
Accuracy: 95.29%
f1 score for each class: [0.97637968 0.98717516 0.89450393 0.94046091]
f1_macro score: 0.95
validation------
Accuracy: 81.78%
f1 score for each class: [0.87228916 0.89076465 0.65708687 0.81055901]
f1_macro score: 0.81
>>
# 0.48792
======================================================
loss_function = "cross_entropy"
layers_dims = [784, 16, 8, num_classes]
activation_fn = ["relu", "relu", "softmax"]
learning_rate = 5e-3
num_iterations = 2000
print_loss = True
print_freq = 20
decrease_freq = 200
decrease_proportion = 0.8
batch_size = 32
>>
Loss after iteration 0: 1.3690034705252072
Loss after iteration 20: 1.0769712212214522
Loss after iteration 40: 0.9644517697072968
Loss after iteration 60: 0.8859669834244982
Loss after iteration 80: 0.8311178951259772
Loss after iteration 100: 0.794971181866314
Loss after iteration 120: 0.7692868412623348
Loss after iteration 140: 0.7509511096347771
Loss after iteration 160: 0.7303338558606144
Loss after iteration 180: 0.7204848871641002
Loss after iteration 200: 0.7087055994450253
Loss after iteration 220: 0.6857184281607243
Loss after iteration 240: 0.676584710412669
Loss after iteration 260: 0.6681899948002987
Loss after iteration 280: 0.6610066675130674
Loss after iteration 300: 0.6562817025772228
Loss after iteration 320: 0.650384969455193
Loss after iteration 340: 0.641948538197214
Loss after iteration 360: 0.6384238417750117
Loss after iteration 380: 0.6321758791908074
Loss after iteration 400: 0.6264219333246633
Loss after iteration 420: 0.6117416996431633
Loss after iteration 440: 0.609747549284696
Loss after iteration 460: 0.60466434392772
Loss after iteration 480: 0.6031159741468158
Loss after iteration 500: 0.5976580659463507
Loss after iteration 520: 0.5961391465949828
Loss after iteration 540: 0.5928438176863666
Loss after iteration 560: 0.5904780026796791
Loss after iteration 580: 0.5873986184414521
Loss after iteration 600: 0.5823130752113233
Loss after iteration 620: 0.5724324614623215
Loss after iteration 640: 0.5715354040848398
Loss after iteration 660: 0.570046006302648
Loss after iteration 680: 0.5674870925902495
Loss after iteration 700: 0.5664061968980207
Loss after iteration 720: 0.5649715159990201
Loss after iteration 740: 0.5633060600297672
Loss after iteration 760: 0.5605902069527091
Loss after iteration 780: 0.5590411517938312
Loss after iteration 800: 0.5576915258365156
Loss after iteration 820: 0.5477572047509869
Loss after iteration 840: 0.5476384380751907
Loss after iteration 860: 0.5446787690671032
Loss after iteration 880: 0.5455484663638936
Loss after iteration 900: 0.5449114784729155
Loss after iteration 920: 0.5411795852532207
Loss after iteration 940: 0.5418966860899821
Loss after iteration 960: 0.542830287188331
Loss after iteration 980: 0.539443716883291
Loss after iteration 1000: 0.5386768996002987
Loss after iteration 1020: 0.5315415695522985
Loss after iteration 1040: 0.530854570086323
Loss after iteration 1060: 0.5293032770043837
Loss after iteration 1080: 0.526875198069108
Loss after iteration 1100: 0.5268159165084149
Loss after iteration 1120: 0.5259877749333101
Loss after iteration 1140: 0.5260416115990141
Loss after iteration 1160: 0.5249713394396123
Loss after iteration 1180: 0.524440532662528
Loss after iteration 1200: 0.5224524778504875
Loss after iteration 1220: 0.5174436420098507
Loss after iteration 1240: 0.5181254627569145
Loss after iteration 1260: 0.5159091454591613
Loss after iteration 1280: 0.5140772767581501
Loss after iteration 1300: 0.5150817578702351
Loss after iteration 1320: 0.5141605547050834
Loss after iteration 1340: 0.5135703276629395
Loss after iteration 1360: 0.5138891927929742
Loss after iteration 1380: 0.5122448798067991
Loss after iteration 1400: 0.5118604978059561
Loss after iteration 1420: 0.5071811444763286
Loss after iteration 1440: 0.5053577111800763
Loss after iteration 1460: 0.5069304251983613
Loss after iteration 1480: 0.5057930393147606
Loss after iteration 1500: 0.5048527041006998
Loss after iteration 1520: 0.5047119796518409
Loss after iteration 1540: 0.5033919490663565
Loss after iteration 1560: 0.5037615045055468
Loss after iteration 1580: 0.5034977719483136
Loss after iteration 1600: 0.502001936563135
Loss after iteration 1620: 0.49815370452224944
Loss after iteration 1640: 0.4977145120896839
Loss after iteration 1660: 0.497534729853507
Loss after iteration 1680: 0.4965265939688542
Loss after iteration 1700: 0.4967202458349737
Loss after iteration 1720: 0.4960169416673269
Loss after iteration 1740: 0.49639291834518895
Loss after iteration 1760: 0.49496151168433716
Loss after iteration 1780: 0.4950701844431964
Loss after iteration 1800: 0.4946721507817721
Loss after iteration 1820: 0.49201809739777014
Loss after iteration 1840: 0.49164566068701177
Loss after iteration 1860: 0.4907082629800437
Loss after iteration 1880: 0.49140122414872833
Loss after iteration 1900: 0.4900350178586568
Loss after iteration 1920: 0.4903776374661964
Loss after iteration 1940: 0.48960095671379983
Loss after iteration 1960: 0.4893886127870765
Loss after iteration 1980: 0.4887135928074742
>>
training------
Accuracy: 81.17%
f1 score for each class: [0.878232   0.90904904 0.61159826 0.8010943 ]
f1_macro score: 0.80
validation------
Accuracy: 73.78%
f1 score for each class: [0.81795998 0.84392476 0.5083167  0.72405312]
f1_macro score: 0.72
>>
# 0.52747
======================================================
loss_function = "cross_entropy"
layers_dims = [784, 8, 4, num_classes]
activation_fn = ["relu", "relu", "softmax"]
learning_rate = 1e-2
num_iterations = 2000
print_loss = True
print_freq = 20
decrease_freq = 100
decrease_proportion = 0.8
batch_size = 16
>>
Loss after iteration 0: 1.3780494940248307
Loss after iteration 20: 1.0641064386009018
Loss after iteration 40: 0.978186706162561
Loss after iteration 60: 0.9224246485326937
Loss after iteration 80: 0.8954831161853496
Loss after iteration 100: 0.8762446998717961
Loss after iteration 120: 0.8580080851029571
Loss after iteration 140: 0.8488091936274255
Loss after iteration 160: 0.8386160532051458
Loss after iteration 180: 0.8334906648366662
Loss after iteration 200: 0.8258344689662034
Loss after iteration 220: 0.8149345205653532
Loss after iteration 240: 0.8114650089751582
Loss after iteration 260: 0.8087796201325665
Loss after iteration 280: 0.8037983073096846
Loss after iteration 300: 0.8004838747141866
Loss after iteration 320: 0.7914691147564754
Loss after iteration 340: 0.7880886935934915
Loss after iteration 360: 0.7850077602432747
Loss after iteration 380: 0.7835874705407692
Loss after iteration 400: 0.7807710232504068
Loss after iteration 420: 0.7737345406953878
Loss after iteration 440: 0.7709943568886589
Loss after iteration 460: 0.7705767411267619
Loss after iteration 480: 0.7678491767412966
Loss after iteration 500: 0.7669206030226194
Loss after iteration 520: 0.7609866391283344
Loss after iteration 540: 0.7594084200260397
Loss after iteration 560: 0.7595614514671819
Loss after iteration 580: 0.7566913314798549
Loss after iteration 600: 0.7563916762055514
Loss after iteration 620: 0.7520851821022287
Loss after iteration 640: 0.7507933505734243
Loss after iteration 660: 0.7500756127634496
Loss after iteration 680: 0.749171442435101
Loss after iteration 700: 0.7486201040615957
Loss after iteration 720: 0.7440576187990591
Loss after iteration 740: 0.7438663572760574
Loss after iteration 760: 0.7436103300692816
Loss after iteration 780: 0.742325438165093
Loss after iteration 800: 0.7420351073264387
Loss after iteration 820: 0.7387885037632272
Loss after iteration 840: 0.7382961046216358
Loss after iteration 860: 0.7381893059509838
Loss after iteration 880: 0.737628201805434
Loss after iteration 900: 0.7363969594993638
Loss after iteration 920: 0.7340101473024484
Loss after iteration 940: 0.7341444025818702
Loss after iteration 960: 0.7331666987757721
Loss after iteration 980: 0.732880576414698
Loss after iteration 1000: 0.7326875643032841
Loss after iteration 1020: 0.7303605535870638
Loss after iteration 1040: 0.7294603961661347
Loss after iteration 1060: 0.7297425649586673
Loss after iteration 1080: 0.7292795871981151
Loss after iteration 1100: 0.7286713423206297
Loss after iteration 1120: 0.7267393973883638
Loss after iteration 1140: 0.7267784010267235
Loss after iteration 1160: 0.7263250881290341
Loss after iteration 1180: 0.7261557577699543
Loss after iteration 1200: 0.7259836383404653
Loss after iteration 1220: 0.724162451049257
Loss after iteration 1240: 0.7242610598033764
Loss after iteration 1260: 0.7240620089259562
Loss after iteration 1280: 0.7235695778967806
Loss after iteration 1300: 0.7236266413687926
Loss after iteration 1320: 0.7223477942587788
Loss after iteration 1340: 0.7222261823460117
Loss after iteration 1360: 0.722004338816028
Loss after iteration 1380: 0.7221184228915996
Loss after iteration 1400: 0.721693448231879
Loss after iteration 1420: 0.7205667159622402
Loss after iteration 1440: 0.7205400512280726
Loss after iteration 1460: 0.7205008550838063
Loss after iteration 1480: 0.7201352588231477
Loss after iteration 1500: 0.7199313560893996
Loss after iteration 1520: 0.719537149311144
Loss after iteration 1540: 0.7191020128355188
Loss after iteration 1560: 0.7192267725965612
Loss after iteration 1580: 0.7190264692510624
Loss after iteration 1600: 0.7186830955504279
Loss after iteration 1620: 0.71842198291525
Loss after iteration 1640: 0.7179731623613428
Loss after iteration 1660: 0.71815633980803
Loss after iteration 1680: 0.7177586704014662
Loss after iteration 1700: 0.7178699692490544
Loss after iteration 1720: 0.7172794787672621
Loss after iteration 1740: 0.7173713089211173
Loss after iteration 1760: 0.717210307228447
Loss after iteration 1780: 0.7170253406147624
Loss after iteration 1800: 0.7168966038618156
Loss after iteration 1820: 0.7166385485650457
Loss after iteration 1840: 0.7163533516489216
Loss after iteration 1860: 0.7163509421429846
Loss after iteration 1880: 0.7160433943214465
Loss after iteration 1900: 0.7161429258302557
Loss after iteration 1920: 0.7161152524039777
Loss after iteration 1940: 0.7158824143667691
Loss after iteration 1960: 0.7157683458227888
Loss after iteration 1980: 0.7157755053849815
>>
training------
Accuracy: 70.76%
f1 score for each class: [0.79495233 0.81211233 0.39763813 0.71918892]
f1_macro score: 0.68
validation------
Accuracy: 65.94%
f1 score for each class: [0.746      0.75462269 0.36664162 0.67117117]
f1_macro score: 0.63
>>
# 0.45684
======================================================
split_ratio = 0.7
loss_function = "cross_entropy"
layers_dims = [784, 32, 64, 16, num_classes]
activation_fn = ["relu", "relu", "relu", "softmax"]
learning_rate = 1e-2
num_iterations = 2000
print_loss = True
print_freq = 50
decrease_freq = 10
decrease_proportion = 0.96
batch_size = 32
>>
Loss after iteration 0: 1.375451587841962
Loss after iteration 50: 0.724547564569397
Loss after iteration 100: 0.5779280310030015
Loss after iteration 150: 0.49344466513452473
Loss after iteration 200: 0.43924475274911334
Loss after iteration 250: 0.39572390108730077
Loss after iteration 300: 0.35968394039921936
Loss after iteration 350: 0.3321430426669131
Loss after iteration 400: 0.30839746943147817
Loss after iteration 450: 0.288939809725799
Loss after iteration 500: 0.27267681541507993
Loss after iteration 550: 0.25952619398598803
Loss after iteration 600: 0.24856235102216886
Loss after iteration 650: 0.24028061942916426
Loss after iteration 700: 0.23400694048391246
Loss after iteration 750: 0.22838830562973983
Loss after iteration 800: 0.22377373463822064
Loss after iteration 850: 0.21933052620504614
Loss after iteration 900: 0.2169952509818057
Loss after iteration 950: 0.2142969547745771
Loss after iteration 1000: 0.212143044007824
Loss after iteration 1050: 0.21077078144246036
Loss after iteration 1100: 0.209300571932773
Loss after iteration 1150: 0.20822400633149526
Loss after iteration 1200: 0.20742410324802424
Loss after iteration 1250: 0.2066326756858868
Loss after iteration 1300: 0.20617156964922334
Loss after iteration 1350: 0.20553656432123646
Loss after iteration 1400: 0.2051677588186209
Loss after iteration 1450: 0.20485389316014607
Loss after iteration 1500: 0.2045285954430907
Loss after iteration 1550: 0.20435805575181368
Loss after iteration 1600: 0.20417559444732275
Loss after iteration 1650: 0.20402524124610805
Loss after iteration 1700: 0.20386757530197758
Loss after iteration 1750: 0.2037801917529154
Loss after iteration 1800: 0.20373293761683225
Loss after iteration 1850: 0.20361901393147167
Loss after iteration 1900: 0.203553865137653
Loss after iteration 1950: 0.2035329084199103
>>
training------
Accuracy: 93.35%
f1 score for each class: [0.96877218 0.9858115  0.84755815 0.91277633]
f1_macro score: 0.93
validation------
Accuracy: 78.62%
f1 score for each class: [0.84054143 0.86410003 0.60202475 0.78873703]
f1_macro score: 0.77
>>
# 0.47520
======================================================
split_ratio = 0.98
loss_function = "cross_entropy"
layers_dims = [784, 16, 16, num_classes]
activation_fn = ["relu", "relu", "softmax"]
learning_rate = 1e-2
num_iterations = 2000
print_loss = True
print_freq = 50
decrease_freq = 100
decrease_proportion = 0.8
batch_size = 64
>>
Loss after iteration 0: 1.3737926535785911
Loss after iteration 50: 0.9081619121459272
Loss after iteration 100: 0.787311555944711
Loss after iteration 150: 0.7272486265893064
Loss after iteration 200: 0.6978174360968356
Loss after iteration 250: 0.6727285389088332
Loss after iteration 300: 0.6559179920016492
Loss after iteration 350: 0.6376602169381618
Loss after iteration 400: 0.6298674635835949
Loss after iteration 450: 0.613170048793149
Loss after iteration 500: 0.6055397233696801
Loss after iteration 550: 0.5949332411710881
Loss after iteration 600: 0.5898702906564768
Loss after iteration 650: 0.5827658769754432
Loss after iteration 700: 0.5775332817084609
Loss after iteration 750: 0.5717108569199876
Loss after iteration 800: 0.5675803073522189
Loss after iteration 850: 0.5627290990733635
Loss after iteration 900: 0.5598774661015451
Loss after iteration 950: 0.5557747697144246
Loss after iteration 1000: 0.5546274748886213
Loss after iteration 1050: 0.5507182436604872
Loss after iteration 1100: 0.5510173255750483
Loss after iteration 1150: 0.5464730679199596
Loss after iteration 1200: 0.5454242637255651
Loss after iteration 1250: 0.543496863181086
Loss after iteration 1300: 0.5433478264218271
Loss after iteration 1350: 0.5414594167841513
Loss after iteration 1400: 0.5404543076927749
Loss after iteration 1450: 0.5384412600949787
Loss after iteration 1500: 0.5380952102409606
Loss after iteration 1550: 0.5369747298111937
Loss after iteration 1600: 0.5364551492332877
Loss after iteration 1650: 0.5346721529988046
Loss after iteration 1700: 0.5346419293237549
Loss after iteration 1750: 0.5340338482350052
Loss after iteration 1800: 0.5335767631256146
Loss after iteration 1850: 0.5333518387114625
Loss after iteration 1900: 0.5330297513432186
Loss after iteration 1950: 0.5323730064354496
>>
training------
Accuracy: 79.80%
f1 score for each class: [0.86850091 0.88233807 0.59780189 0.78870011]
f1_macro score: 0.78
validation------
Accuracy: 72.49%
f1 score for each class: [0.77866667 0.85714286 0.48231511 0.73271889]
f1_macro score: 0.71
>>
# 0.46815
======================================================
# 
======================================================
# 
======================================================
# 
======================================================
# 
======================================================
training------
Accuracy: 99.86%
f1 score for each class: [0.99811174 0.99966559 0.99691557 0.99916976]
f1_macro score: 1.00
validation------
Accuracy: 83.58%
f1 score for each class: [0.89150712 0.89332684 0.68228808 0.83142715]
f1_macro score: 0.82
