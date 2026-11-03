# Independentendpointk8:PASS

Actualcompletegraph (72,3),n=173250,m=5966400. Exactn mheader/strictlexbody/simplelabels checked. Every5121600oldsourceedge retainedexactly; all844800newedges joinoldsource tonewlabels,0newnew. All13200literalnewN64sets exactlyequaltheirimmutablefilledsourcecenterN. sourceoldlabelcutis160050,including50originalfills. Degree64count67650,degree72count105600; sourcepinload8at105600oldvertices,0at54450.

Shared../../PROOF.md givesallpairsandallprefixcurrentR2pincoverage withinteriorsonlyinthefixed160050source,includingitsoriginalfillnodes. Repeatedcentersuseanoldcommonneighbor; adjacentcentersusethethree-edgeold-centerroute. Nofuturecloneorcenterindependenceisassumed. CollapseHomtosourcepreservesnonD2. Thusdegreecap72andexactD3holdforthisendpoint independentlyofthemaximalBFS.

SourceR2wasenumeratedonceforeach1650centersbeforeanynewfileinput,R=3185for33centersand3248for1617;sourceR3inferredfromacceptedD3. Histogramformula(1,64,R+8,159985−R+13192)givesproof-derivedclasses[{'histogram': [1, 64, 3193, 169992], 'roots': 264}, {'histogram': [1, 64, 3256, 169929], 'roots': 12936}]. Only thismaxcasehasactualnewrootBFS:all13200roots,actualhistograms[{'histogram': [1, 64, 3193, 169992], 'roots': 264}, {'histogram': [1, 64, 3256, 169929], 'roots': 12936}],eachdistclassmatchespriorpercenterprediction.

LiteralbindingCPU1.29446,newBFSCPU11.1961;overallfamily21.419453053CPU includingonecompile/sourceparse/R2prediction/eightbindings/maxBFS/aggregation,below180budget.0oldR3/field/geometry/Leanchecksrepeated. Allsharedprocessesterminal. Comparedwithseparatelycheckedpublished-methodguarantee173200,advantage50;globalpriorityandnewconcreteLeanarenotclaimedhere.
