"""
Gulls Parser


lc file, 1L example:
```
#fs: 0.968348 0.946456 0.911917 
#Sourcemag: 35.569 26.1783 22.2303 19.5046 19.3117 17.7303 16.953 16.5804 14.7459 19.0443 16.0382 56.6457 49.9228 39.6881 28.2065 34.344 36.259 30.3846 24.8681 55.0022 45.9351 34.6905 29.4874 23.2458 33.5654 40.8896 28.3719 25.2227 22.0606 18.7631 16.0049 14.7423 
#Sourcedata: 29650 -8.64531 2.26471 45.238 61.677 -94.5465 96.4017 0.923965 2 10 4730.68 2.46395 0 0.922167 0.767067 9.32001 -0.517316 0.410646 -0.589734 267.223 -28.8905 8.30801 0.129165 0.0595409 -0.0857799 13.7366 0 
#Obssrcmag: 19.3117 26.1783 16.5804 
#Lensmag: 41.1432 31.7535 27.8141 25.0951 24.9053 23.3287 22.5571 22.1803 20.3458 24.6343 21.6396 62.341 55.5064 45.2886 33.7794 39.9088 41.8314 35.9557 30.4466 60.7074 51.5473 40.2557 35.0583 28.8283 39.1386 46.4692 33.9421 30.8016 27.6474 24.3546 21.6066 20.3424 
#Lensdata: 43423 -3.09634 1.8829 214.067 228.69 127.933 77.5453 0.694459 0 10 4769.48 4.61032 0 0.694385 6.40544 0.683356 -0.202709 0.400301 -0.60246 267.229 -28.9059 8.11897 -0.0598735 0.0567201 -0.0852444 13.7366 0 
#Obslensmag: 24.9053 31.7535 22.1803 
#Planet: 0.0100746 4.60334 43.4864 276.997 0.0145087 3.26534 11.7674 
#Event: 0.92019 327.325 110.655832887 163.519043955 -0.296902 2.2893 8.33479 0.0411327 
#Obsgroup: 0 3.51242e+06 0 1044.31 0 1 2 
Simulation_time measured_relative_flux measured_relative_flux_error true_relative_flux true_relative_flux_error observatory_code saturation_flag best_single_lens_fit parallax_shift_t parallax_shift_u BJD source_x source_y lens1_x lens1_y lens2_x lens2_y parallax_shift_x parallax_shift_y parallax_shift_z 
112.505968565 1.3672988 0.00417313 1.36523069019 0.00417313 0 0 1.3648701 5.32418e-06 7.2705e-06  2458346.5059686 0.636933 0.65473 -0.0466982 0 3.21864 0 0.816725 -0.615553 -0.00467182 
112.51440037 1.3660998 0.00417283 1.36504720547 0.00417283 0 0 1.3646689 5.37296e-06 7.33719e-06  2458346.5144004 0.637785 0.654184 -0.0466982 0 3.21864 0 0.816811 -0.615435 -0.00467123 
112.522832176 1.3606156 0.00417252 1.36486304973 0.00417252 0 0 1.3644672 5.42197e-06 7.4042e-06  2458346.5228322 0.638636 0.653638 -0.0466982 0 3.21864 0 0.816897 -0.615317 -0.00467063 
112.531263981 1.3609597 0.00417222 1.36467822502 0.00417222 0 0 1.364265 5.4712e-06 7.47151e-06  2458346.5312640 0.639488 0.653092 -0.0466982 0 3.21864 0 0.816983 -0.6152 -0.00467003 
```

master df, 1L example:
```
   EventID  SubRun  Field  galactic_l  galactic_b      ra_deg    dec_deg  SourceID  Source_mul  Source_mub   Source_Vr    Source_U    Source_V    Source_W  Source_iMass  Source_CL  Source_age  Source_Teff  Source_logg  Source_pop  Source_Mass  Source_Mbol  Source_Radius  Source_Fe_H  Source_l  Source_b  Source_RA20000  Source_DEC20000  Source_Dist  Source_x  Source_y  Source_z  Source_Av  Source_alpha_Fe  LensID   Lens_mul  Lens_mub     Lens_Vr      Lens_U      Lens_V      Lens_W  Lens_iMass  Lens_CL  Lens_age  Lens_Teff  Lens_logg  Lens_pop  Lens_Mass  Lens_Mbol  Lens_Radius  Lens_Fe_H    Lens_l    Lens_b  Lens_RA20000  Lens_DEC20000  Lens_Dist    Lens_x    Lens_y    Lens_z   Lens_Av  Lens_alpha_Fe   u0lens1       alpha     t0lens1        tref      tcroin    ucroin     rcroin     tE_ref   tE_helio        rE    thetaE       rho       piE      piEN      piEE  murel_helio_alpha  murel_helio_delta  murel_helio_l  murel_helio_b  murel_helio_lambda  murel_helio_beta  murel_helio  murel_ref_alpha  murel_ref_delta  murel_ref_l  murel_ref_b  murel_ref_lambda  murel_ref_beta  murel_ref  vtilde_helio    vtilde_ref      v_ref  vtilde_helio_N  vtilde_helio_E  vtilde_ref_N  vtilde_ref_E   v_ref_N    v_ref_E     piEll     piErp          vt  LDgamma  Planet_mass  Planet_semimajoraxis  Planet_inclination  Planet_orbphase  Planet_q  Planet_s  Planet_period  u0max  t0range  weight_scale  raw_weight    weight  Source_R062  Source_Z087  Source_Y106  Source_J129  Source_W146  Source_H158  Source_F184  Source_K213  Source_2MASS_Ks  Source_2MASS_J  Source_2MASS_H  Source_Bessell_U  Source_Bessell_B  Source_Bessell_V  Source_Bessell_I  Source_Bessell_R  Source_Kepler_Kp  Source_TESS  Source_DECam_z  Source_DECam_u  Source_DECam_g  Source_DECam_r  Source_DECam_i  Source_DECam_Y  Source_Gaia_G_EDR3  Source_Gaia_BP_EDR3  Source_Gaia_RP_EDR3  Source_VISTA_Z  Source_VISTA_Y  Source_VISTA_J  Source_VISTA_H  Source_VISTA_Ks  Lens_R062  Lens_Z087  Lens_Y106  Lens_J129  Lens_W146  Lens_H158  Lens_F184  Lens_K213  Lens_2MASS_Ks  Lens_2MASS_J  Lens_2MASS_H  Lens_Bessell_U  Lens_Bessell_B  Lens_Bessell_V  Lens_Bessell_I  Lens_Bessell_R  Lens_Kepler_Kp  Lens_TESS  Lens_DECam_z  Lens_DECam_u  Lens_DECam_g  Lens_DECam_r  Lens_DECam_i  Lens_DECam_Y  Lens_Gaia_G_EDR3  Lens_Gaia_BP_EDR3  Lens_Gaia_RP_EDR3  Lens_VISTA_Z  Lens_VISTA_Y  Lens_VISTA_J  Lens_VISTA_H  Lens_VISTA_Ks  Obs_0_fs  Obs_1_fs  Obs_2_fs  NumObsGroups  ErrorFlag  ObsGroup_0_flatlc  ObsGroup_0_flatchi2  ObsGroup_0_FiniteSourceflag  ObsGroup_0_chi2  LCOutput  final_weight
0       67       1    841    1.256491   -2.222655  269.322434 -28.990953     36560   -7.210024    1.255378  108.175950  129.177600  -45.486549   54.437108      0.804417        0.0   10.000000    5582.0587     4.483490         0.0     0.804231     5.250149       0.849295    -0.389547  1.199719 -2.203201       269.26951       -29.030326     8.585859  0.398926  0.179634 -0.330902   1.669085              0.0    8751  -4.644164  2.260397   46.873555   66.514373   79.824871   87.022600    0.229608      0.0      10.0  3349.3886   5.017572       0.0   0.229605  10.166270     0.245184  -0.028571  1.202757 -2.201022     269.26909     -29.026607   7.579223 -0.606659  0.158974 -0.289824  1.669085            0.0  0.418063  303.083675  113.588110  113.588110  147.849163 -0.355954   2.653872  22.595860  22.594310  1.291994  0.170465  0.002698  0.090746  0.090032  0.011362           0.413166           2.724518       2.565860       1.005020            0.400284          2.726440     2.755668         0.357910         2.732135     2.544817     1.056678          0.344992        2.733796   7.592663    844.470146    844.412235  17.093522      835.513464      122.666533    837.767758    105.722310 -2.254293  16.944222  0.015260 -0.089454   99.008606      0.0     0.000997              2.713747            6.212203       180.292022  0.004344  2.100433       9.309417    3.0    210.0           1.0    0.937457  1.616858    22.303768    21.020207    20.544607    20.245277    20.279845    20.104701    20.184883    20.373589        18.539084       19.400535       18.727550         25.501579         24.694833         22.908904         20.897439         21.939395         22.313225    21.244824       20.861041       25.846589       23.888135       22.151249       21.436656       20.658636           22.053416            23.217320            21.000187       20.472469       19.987568       19.344530       18.727326        18.541821  28.144972  25.587534  24.716085  24.183185  24.187690  23.856564  23.872680  23.881873      22.047368     23.356864     22.408061       33.792368       31.933426       29.371548       25.705951       27.695151       27.958787  26.161751     25.297503     33.421171     30.781668     28.099146     26.350571     24.953887         27.630620          29.731658          25.969156     25.008807     24.234665     23.280596     22.417210      22.067713  0.675514  0.786392  0.285744             1          0                  0         2.219690e+07                            0     7.001199e+02         0      0.099660
1       76       1    841    1.170004   -2.264559  269.314493 -29.086746     27598   -3.092268   -1.168290  -24.068608  -10.463363  124.305800  -36.845009      0.325045        0.0   10.000000    3099.0345     4.877384         0.0     0.325025     9.774446       0.343032     0.407872  1.199404 -2.202307       269.26844       -29.030150     8.239452  0.052887  0.172341 -0.316737   1.669085              0.0   24434 -12.732075 -0.622578 -204.639270 -182.166110 -250.440950   -7.978568    0.337332      0.0      10.0  3011.3580   4.854754       0.0   0.337322   9.797360     0.359485   0.510902  1.203982 -2.203479     269.27222     -29.026777   8.148870 -0.037622  0.171097 -0.313234  1.669085            0.0  0.395149  229.654620  168.607977  168.607977  168.607977  0.251658   1.570180   2.320796   2.320280  0.499817  0.061336  0.003156  0.021996 -0.018454 -0.011969          -5.294372          -8.074237      -9.639807       0.545708           -5.255695         -8.099466     9.655241        -5.291554        -8.073520    -9.637776     0.543627         -5.252881       -8.098735  93.182265  33926.336588  33918.799735  10.217435   -28459.694417   -18467.325416 -28457.126192 -18457.436018 -2.568224  -9.889398 -0.011642  0.018662  372.976922      0.0     0.005000              0.876284           59.322319       248.052058  0.014823  1.057240       1.402006    3.0    210.0           1.0    1.175740  2.027519    28.578175    25.530777    24.433898    23.866963    23.901972    23.575048    23.611813    23.566180        21.731675       23.013826       22.109671         34.029645         32.524576         30.091810         25.791586         28.158035         28.254955    26.184513       25.159401       33.450671       31.360550       28.712909       26.471066       24.717230           27.859773            30.440404            26.049122       24.961298       23.985449       22.931134       22.122830        21.757954  28.788272  25.602540  24.420752  23.839304  23.886403  23.563088  23.601968  23.534460      21.699955     22.974784     22.091290       34.226666       32.819718       30.411197       25.917510       28.375787       28.428628  26.272278     25.199768     33.565838     31.644534     28.973122     26.601582     24.721497         28.010943          30.751583          26.159273     25.037507     23.984751     22.889279     22.105762      21.728158  0.144271  0.143057  0.049190             1          0                  0         6.575030e+04                            0     1.313896e+03         0      0.124972
2       84       1    841    1.271671   -2.299232  269.406936 -29.016096     31455   -5.411557    4.149923 -171.945650 -147.703340   27.519658  179.229710      1.013547        0.0   10.000000    5386.5880     4.310267         0.0     1.013254     4.716438       1.166170     0.496391  1.197919 -2.205375       269.27063       -29.032970     8.368023  0.181310  0.174813 -0.322392   1.669085              0.0    3500 -10.404396 -1.838702   76.850724   94.594978 -109.448960  -58.330325    0.290776      0.0      10.0  3145.2921   4.944815       0.0   0.290772  10.040774     0.294578   0.296345  1.200969 -2.201428     269.26847     -29.028357   7.231825 -0.953693  0.151462 -0.275812  1.669085            0.0  0.273929  163.623397  178.265612  178.265612  186.596971  0.011951  12.813264  10.092309  10.106797  1.560252  0.215748  0.003004  0.087024 -0.081317  0.030994           2.693405          -7.316942      -4.992837      -5.988627            2.723654         -7.305736     7.796927         2.750681        -7.307564    -4.956099    -6.033558          2.780891       -7.296121  60.966736   1968.617829   1971.443878  14.654039    -1844.598790      687.685583  -1842.171114    702.137131 -2.427676 -14.451548  0.033437  0.080344  267.296216      0.0     0.013573              1.258564          -67.893840       163.314482  0.046678  0.777578       2.559352    3.0    210.0           1.0    3.288469  5.680245    21.666671    20.349184    19.858991    19.536969    19.579076    19.399699    19.473613    19.647780        17.813275       18.696015       18.022430         25.489186         24.276316         22.316185         20.226215         21.282849         21.685134    20.576865       20.189354       25.797213       23.375599       21.494367       20.768006       19.975583           21.438431            22.662012            20.331961       19.801597       19.292854       18.635621       18.022827        17.816036  28.430830  25.460144  24.421026  23.862425  23.891129  23.559586  23.601895  23.564443      21.729938     23.015582     22.097595       33.963774       32.355385       29.885923       25.686978       28.004585       28.125331  26.106143     25.109841     33.389270     31.181967     28.538509     26.365454     24.693738         27.743836          30.240645          25.956170     24.888185     23.967661     22.934521     22.110293      21.755670  0.039086  0.055204  0.030463             1          0                  0         6.323215e+05                            0     1.202492e+04         0      0.350118
3      112       1    841    1.171237   -2.252799  269.303547 -29.079797     42894   -8.731954    1.247576   54.674126   77.653262 -131.959260   59.628493      0.824670        0.0   10.000000    5009.5166     4.523736         0.0     0.824549     5.792363       0.821510     0.128557  1.201379 -2.203812       269.27106       -29.029195     9.151944  0.964414  0.191742 -0.353937   1.669085              0.0   18324  -7.091714 -1.133051   96.486004  113.175590  -19.392283  -38.765443    0.326446      0.0      10.0  3399.8352   4.915845       0.0   0.326435   9.460214     0.329396   0.118425  1.204886 -2.199097     269.26840     -29.023801   7.943477 -0.242779  0.166910 -0.304304  1.669085            0.0  1.184518   97.786807  145.528189  145.528189  146.614714 -0.192471   3.906257  26.721195  26.669846  1.676819  0.211094  0.001977  0.078747  0.006890  0.078445           2.881878           0.229239       1.640241      -2.380626            2.880730          0.243240     2.890981         2.875553         0.238482     1.645080    -2.370526          2.874360        0.252451   8.325679    824.433441    822.849148   3.193814       69.365682      821.510134     71.992666    819.693708 -2.626985   1.816426  0.078483 -0.006444  108.862242      0.0     0.002640              0.697134          -13.612405       181.972786  0.008088  0.415735       1.014675    3.0    210.0           1.0    1.215630  2.092745    23.027037    21.612391    21.074364    20.699739    20.717577    20.484513    20.527727    20.706615        18.872110       19.873184       19.088066         27.090871         25.765563         23.727503         21.514644         22.630993         23.042035    21.872156       21.437385       27.381536       24.834914       22.846987       22.062763       21.208340           22.794436            24.078669            21.629049       21.059607       20.519688       19.809058       19.089931        18.875540  27.544797  24.985707  24.105728  23.578685  23.581545  23.255317  23.263188  23.286683      21.452178     22.752494     21.808238       33.011410       31.256244       28.769413       25.107924       27.101783       27.358738  25.559311     24.692622     32.692155     30.131093     27.506814     25.753272     24.342099         27.028073          29.127731          25.368862     24.409640     23.621821     22.676915     21.816785      21.471074  0.579639  0.681738  0.254154             1          0                  0         2.161401e+05                            0     1.091723e+03         0      0.128992
4      166       1    841    1.212941   -2.273487  269.347887 -29.054059     49725   -6.285243   -0.232855   20.416056   41.100086 -155.949010   -7.944549      0.960809        0.0    7.538225    6273.5222     4.104305         9.0     0.960560     3.597599       1.439244    -0.711782  1.198050 -2.194229       269.25967       -29.027278    13.493922  5.301977  0.281929 -0.527667   1.669085              0.0   27620  -7.753827  2.228839 -246.383860 -223.312930  -63.141655  104.962270    0.660795      0.0      10.0  4584.4061   4.631959       0.0   0.660736   6.686218     0.649931  -0.214339  1.204458 -2.199405     269.26846     -29.024326   8.262527  0.075939  0.173552 -0.317253  1.669085            0.0 -0.179852   74.094860  162.771274  162.771274  164.997715  0.048501  14.855795  67.068585  65.445831  4.243779  0.513618  0.000966  0.091354 -0.000928 -0.091349          -2.866181          -0.041047      -1.468585       2.461694           -2.865964         -0.054087     2.866475        -2.797075        -0.015694    -1.412076     2.414522         -2.796975       -0.028419   7.823875    289.603050    282.595974   7.436873       -5.464431     -289.551492     -2.871221   -282.581388 -2.593210  -6.970104 -0.091334  0.001911  112.274841      0.0     0.029454              6.811499          -33.400050       207.386400  0.044578  1.552746      21.398318    3.0    210.0           1.0    2.881029  4.849096    21.665448    20.506210    20.084079    19.847598    19.895484    19.777388    19.886901    20.082176        18.247671       18.987154       18.416858         24.371796         23.767595         22.200242         20.358313         21.326471         21.666043    20.693392       20.361079       24.655820       23.074859       21.535137       20.890022       20.181004           21.390443            22.455279            20.448614       19.961504       19.520024       18.937184       18.414955        18.249400  23.837462  22.285261  21.685849  21.248946  21.232941  20.940581  20.946605  21.122583      19.288078     20.439131     19.522096       28.322971       26.779570       24.623724       22.218503       23.420482       23.845527  22.586206     22.091606     28.546908     25.815373     23.644543     22.775418     21.843066         23.595506          24.976591          22.346024     21.728260     21.147478     20.371292     19.525603      19.292457  0.722850  0.846831  0.337726             1          0                  0         1.692747e+08                            0     2.323244e+07         0      0.298888
```

"""

from os import path
import pathlib
import pandas as pd
import numpy as np
from io import StringIO

class GullsParser:
    def __init__(self, input_dir="input", output_dir="output"):
        """
        data (DataFrame) with the columns:
          - Simulation_time
          - measured_relative_flux
          - measured_relative_flux_error
          - true_relative_flux
          - true_relative_flux_error
          - observatory_code
          - saturation_flag
          - best_single_lens_fit
          - parallax_shift_t
          - parallax_shift_u
          - BJD
          - source_x
          - source_y
          - lens1_x
          - lens1_y
          - lens2_x
          - lens2_y
          - parallax_shift_x
          - parallax_shift_y
          - parallax_shift_z

        1L dic contains:
        * data (DataFrame) with the full lc data
        * BJD (Numpy array) with the Barycentric Julian Date of the observations
        * obs (int) filter code of the observations
        * mag (Numpy array) with the magnitudes of the observations
        * mag_err (Numpy array) with the errors of the magnitudes
        * FL_0 (float) from the lc comments (Obslensmag)
        * FL_1 (float) from the lc comments (Obslensmag)
        * FL_2 (float) from the lc comments (Obslensmag)
        * FS_0 (float) from the lc comments (fs)
        * FS_1 (float) from the lc comments (fs)
        * FS_2 (float) from the lc comments (fs)
        * t0 (float)
        * tE (float)
        * u0 (float)
        * rho (float)
        * pi_EN (float)
        * pi_EE (float)
        """
        self.input_dir = pathlib.Path(input_dir)
        self.output_dir = pathlib.Path(output_dir)

        self.single_lens_dir = self.input_dir / "1L"
        self.binary_lens_dir = self.input_dir / "2L"
        self.triple_lens_dir = self.input_dir / "3L"

        self.output_single_lens_dir = self.output_dir / "1L"
        self.output_binary_lens_dir = self.output_dir / "2L"
        self.output_triple_lens_dir = self.output_dir / "3L"

        self.master_column_mapping = {
            "t0_lens1": "t0",
            "tE_ref": "tE",
            "u0_lens1": "u0",
            "rho": "rho",
            "piEN": "pi_EN",
            "piEE": "pi_EE"
        }  # gulls_key: df_key

        self.additional_master_columns_for_2L = {
            "q": "q",
            "s": "s",
            "alpha": "alpha"
        }

        self.additional_master_columns_for_3L = {
            "q3": "q3",
            "s3": "s3",
            "psi": "psi"
        }

        self.filters = ["F146", "F087", "F213"]  # Observatories codes

    @staticmethod
    def concatenate_master_df(path_list):
        """
        Concatenate a list of DataFrames into a single master DataFrame.
        """
        df_list = []

        for p in path_list:
            if not pathlib.Path(p).exists():
                raise FileNotFoundError(f"File not found: {p}")
            
            # Load all DataFrames from the list of paths and concatenate them
            df = GullsParser.read_master(p)
            df_list.append(df)

        return pd.concat(df_list, ignore_index=True)
    
    #static method to read hdf5 or csv based on suffix
    @staticmethod
    def read_master(path):
        """ Read a master DataFrame from a file, which can be either .csv or .hdf5.
        Args:
            path (str or pathlib.Path): Path to the master file.
        Returns:
            pd.DataFrame: Loaded DataFrame.
        """
        if path.suffix == ".hdf5":
            return pd.read_hdf(path)
        else:
            return pd.read_csv(path)

    @staticmethod
    def load_master(path):
        """
        Load the master DataFrame for a given lens type.
        """
        #if is a string or pathlib.Path
        if isinstance(path, str):
            path = pathlib.Path(path)
            if not path.exists():
                raise FileNotFoundError(f"Master file not found: {path}")
            # Load the DataFrame
            return GullsParser.read_master(path)
        elif isinstance(path, pathlib.Path):
            if not path.exists():
                raise FileNotFoundError(f"Master file not found: {path}")
            # Load the DataFrame
            return GullsParser.read_master(path)
        elif isinstance(path, list):
            # If a list of paths is given, load all DataFrames and concatenate them
            return GullsParser.concatenate_master_df(path)
        else:
            raise TypeError("Path must be a string, pathlib.Path, or list of paths.")
        
    def load_single_lens_master(self):
        """
        Load the master file(s) for single lens systems and save them as a class attribute.
        """
        # master files are all files ending in .csv, or .out, or .hdf5
        master_files = list(self.single_lens_dir.glob("*.csv")) + list(self.single_lens_dir.glob("*.out")) + list(self.single_lens_dir.glob("*.hdf5"))
        if not master_files:
            raise FileNotFoundError(f"No master files found in: {self.single_lens_dir}")

        # Load the master DataFrame(s) and concatenate them if multiple
        self.single_lens_master = self.load_master(master_files)

    def load_binary_lens_master(self):
        """
        Load the master file(s) for binary lens systems and save them as a class attribute.
        """
        # master files are all files ending in .csv, or .out
        master_files = list(self.binary_lens_dir.glob("*.csv")) + list(self.binary_lens_dir.glob("*.out"))
        if not master_files:
            raise FileNotFoundError(f"No master files found in: {self.binary_lens_dir}")

        # Load the master DataFrame(s)
        self.binary_lens_master = self.load_master(master_files)

    def load_triple_lens_master(self):
        """
        Load the master file(s) for triple lens systems and save them as a class attribute.
        """
        # master files are all files ending in .csv, or .out
        master_files = list(self.triple_lens_dir.glob("*.csv")) + list(self.triple_lens_dir.glob("*.out"))
        if not master_files:
            raise FileNotFoundError(f"No master files found in: {self.triple_lens_dir}")

        # Load the master DataFrame(s)
        self.triple_lens_master = self.load_master(master_files)

    @staticmethod
    def save_lc_output(df, output_path, header, comment_text=""):
        """
        Save the processed DataFrame to the output directory.

        file contains:
         * comment lines starting with '#'
         * header line with column names (using lc_column_mapping)
         * data lines
        """
        with open(output_path, 'w') as f:
            # Write comment lines
            for line in comment_text.splitlines():
                f.write(f"# {line}\n")
            # Write header
            f.write(",".join(header) + "\n")
            # Write DataFrame
            df.to_csv(f, index=False)
            f.write("\n")

        print(f"Saved processed data to: {output_path}")

    @staticmethod
    def load_lc_file(file_path):
        """
        Load a light curve file (.lc or .dat) and return the DataFrame, comment text, and header.
        
        The lightcurve columns are:
          Simulation_time measured_relative_flux measured_relative_flux_error true_relative_flux true_relative_flux_error 
          observatory_code saturation_flag best_single_lens_fit parallax_shift_t parallax_shift_u BJD source_x source_y 
          lens1_x lens1_y lens2_x lens2_y
        
        Magnitudes can be computed using:
          m = m_source + 2.5 log f_s - 2.5 log(F)
        where F=fs*mu + (1-fs) is the relative flux (in the file), mu is the magnification, and
          sigma_m = 2.5/ln(10) sigma_F/F
        these are listed in the header information in lines #fs and #Obssrcmag with order matching the observatory code order. 
        The observatory codes correspond to 0=W146, 1=Z087, 2=K213
        """
        if not file_path.exists():
            raise FileNotFoundError(f"Data file not found: {file_path}")

        # Read the file
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Extract comment lines and header
        comment_lines = [line for line in lines if line.startswith("#")]
        header_line = next((line for line in lines if not line.startswith("#")), None)
        
        if header_line is None:
            raise ValueError("No header found in the file.")

        # Split header by whitespace (not comma)
        header = header_line.strip().split()
        
        # Load the data into a DataFrame
        data_lines = [line for line in lines if not line.startswith("#") and line.strip() != header_line.strip()]
        
        # Create a StringIO object with space-separated data
        data_text = "".join(data_lines)
        df = pd.read_csv(StringIO(data_text), sep=r'\s+', names=header)

        # Join comment lines into a single string
        comment_text = "\n".join(comment_lines)

        return df, comment_text, header

    @staticmethod
    def get_magnitudes(F, fs, ms, observatory_codes):
        """
        Calculate the magnitudes from the DataFrame using the formula:
        m = m_source + 2.5 * log10(f_s) - 2.5 * log10(F)
        where F = fs * mu + (1 - fs) is the relative flux.

        Parameters:
        - F: Numpy array of relative flux values.
        - fs: List of flux scaling factors for each observatory.
        - ms: List of source magnitudes for each observatory.
        - observatory_codes: List of observatory codes corresponding to fs and ms.
        
        Returns:
        - A DataFrame with additional columns for magnitudes and their errors.
        """
        if len(fs) != len(observatory_codes) or len(ms) != len(observatory_codes):
            raise ValueError("Length of fs and ms must match the number of observatory codes.")
        
        # Calculate the magnitudes
        mag = ms[observatory_codes] + 2.5 * np.log10(fs[observatory_codes]) - 2.5 * np.log10(F)

        # Calculate the errors in magnitudes
        mag_err = 2.5 / np.log(10) * (F * fs[observatory_codes]) / F**2
        mag_err = np.sqrt(mag_err**2 + (2.5 / np.log(10) * fs[observatory_codes] / F)**2)

        return mag, mag_err
    
    @staticmethod
    def get_zeropoint(elements, table_path="input/Roman_zeropoints_20240301.ecsv"):
        """
        Look up the AB zero point for the flux calculation based on the elements.
        
        Parameters:
        - elements: List of elements (as they appear in the roman technical information table).
        Returns:
        - A dictionary with observatory codes as keys and their corresponding zero points as values.
        """
        # Check if the table path exists
        if not path.exists(table_path):
            # curl the table from the URL if it does not exist
            print(f"Zero point table not found at {table_path}. Downloading from URL.")
            
            # Use requests to download the table from the URL
            import requests
            url = "https://github.com/rges-pit/roman-technical-information/blob/main/data/WideFieldInstrument/Imaging/ZeroPoints/Roman_zeropoints_20240301.ecsv"
            response = requests.get(url)
            if response.status_code == 200:
                # Save the content to the specified path
                table_path = pathlib.Path(table_path)
                with open(table_path, 'wb') as f:
                    f.write(response.content)
            else:
                raise ValueError(f"Failed to retrieve zero point table from URL: {url}")

        # Load the zero point table
        """
        # %ECSV 1.0
        # ---
        # datatype:
        # - {name: detector, datatype: string}
        # - {name: element, datatype: string}
        # - {name: VegaMag, datatype: float64}
        # - {name: ABMag, datatype: float64}
        # - {name: STMag, datatype: float64}
        # - {name: FLAM, datatype: float64}
        # - {name: FNU, datatype: float64}
        # - {name: PHOTLAM, datatype: float64}
        # - {name: PHOTNU, datatype: float64}
        # meta: !!omap
        # - {comments: "Zero points for each detector and imaging optical element (filter) using effective area curves as of 2024 03 01.\nThe\
        #     \ zeropoints are computed using synphot version 1.4.0. The method unit_response() \ndetermines the flux density that generates a\
        #     \ count rate of 1 count per second through \nthe bandpass. This is computed as:\n\n\\dfrac{hc}{\\int P_\\lambda \\lambda d\\lambda}\n\
        #     \nwhere h is the Planck constant, c is the speed of light, P is the effective \narea, and lambda is the wavelength. The integrals\
        #     \ are approximated using the trapezoid \nmethod. Conversions to other units are performed at the pivot wavelength, which is a \n\
        #     measure of the effective wavelength of the bandpass. The pivot wavelength is defined as:\n\n\\sqrt{\\dfrac{\\int P_\\lambda \\lambda\
        #     \ d\\lambda}{\\int (P_\\lambda / \\lambda) d\\lambda}}"}
        # schema: astropy-2.0
        detector element VegaMag ABMag STMag FLAM FNU PHOTLAM PHOTNU
        WFI01 F062 26.417663323428016 26.57551933086481 26.880632649382186 6.423133376578637e-20 8.507310180127394e-31 2.0375262991355374e-08 2.6986623522593194e-19
        WFI01 F087 25.626924239161607 26.22624275057486 27.242258374678336 4.603590128457495e-20 1.1735535182435983e-30 2.0259717908486147e-08 5.16463511448471e-19
        ...
        """
        # Read the table into a DataFrame
        if table_path.suffix == ".ecsv":
            zp_table = pd.read_csv(table_path, comment='#', delim_whitespace=True)

        zp = np.zeros(len(elements))

        for i, element in enumerate(elements):
            if element not in zp_table['element'].values:
                raise ValueError(f"Element '{element}' not found in the zero point table.")
            # get the "ABMag" column value for the <element> row
            abmag = zp_table.loc[zp_table['element'] == element, 'ABMag'].values[0]
            zp[i] = abmag

        return zp
    
    @staticmethod
    def get_fluxes(mag, mag_err, observatory_codes, zp):
        """
        Calculate the fluxes from the magnitudes using the formula:
        F = 10 ** ((zp - m) / 2.5)
        
        Parameters:
        - mag: Numpy array of magnitudes.
        - mag_err: Numpy array of magnitude errors.
        - observatory_codes: List of observatory codes corresponding to the magnitudes.
        - zp: Zero point for the flux calculation.
        
        Returns:
        - A DataFrame with additional columns for fluxes and their errors.
        """
        if len(mag) != len(observatory_codes):
            raise ValueError("Length of mag must match the number of observatory codes.")
        
        # Calculate the fluxes
        F = 10 ** ((zp[observatory_codes] - mag) / 2.5)
        
        # Calculate the errors in fluxes
        F_err = (F * mag_err) / (2.5 * np.log(10))
        
        return F, F_err

    def process_single_lens(self, add_astrometry=True):
        """
        Process single lens data and save the output.
        """
        # load master file(s) with meta data (.csv, .out, .hdf5)
        self.load_single_lens_master()

        # load data files (.lc,  .dat)
        data_files = list(self.single_lens_dir.glob("*.lc")) + list(self.single_lens_dir.glob("*.dat"))
        if not data_files:
            raise FileNotFoundError(f"No data files found in: {self.single_lens_dir}")
        
        # Process each data file
        for data_file in data_files:

            # Strip the file name to get the SubRun, EventID, and Field
            file_name = data_file.stem
            parts = file_name.split("_")
            SubRun = parts[-3]
            Field = parts[-2]
            EventID = parts[-1] 

            # get row from master file based on SubRun, Field, and EventID
            row = self.single_lens_master[
                (self.single_lens_master["SubRun"] == SubRun) &
                (self.single_lens_master["Field"] == Field) &
                (self.single_lens_master["EventID"] == EventID)
            ]

            if row.empty:
                raise ValueError(f"No matching row found in master file for SubRun: {SubRun}, Field: {Field}, EventID: {EventID}")

            # Load the data file
            df, comment_text, header = GullsParser.load_lc_file(data_file)

            dic = {
                "row": row,
                "data": df,
                "BJD": df["BJD"].to_numpy(),
                "obs": df["observatory_code"].to_numpy()
            }

            # Extract parameters from comment text
            for line in comment_text.splitlines():
                if "Obslensmag" in line:
                    parts = line.split()
                    dic["ml_0"] = float(parts[1])
                    dic["ml_1"] = float(parts[2])
                    dic["ml_2"] = float(parts[3])
                    dic["ml"] = [float(m) for m in parts[1:]]
                elif "fs" in line:
                    parts = line.split()
                    dic["FS_0"] = float(parts[1])
                    dic["FS_1"] = float(parts[2])
                    dic["FS_2"] = float(parts[3])
                    dic["fs"] = [float(f) for f in parts[1:]]
                elif "Obssrcmag" in line:
                    parts = line.split()
                    dic["ms_0"] = float(parts[1])
                    dic["ms_1"] = float(parts[2])
                    dic["ms_2"] = float(parts[3])
                    dic["ms"] = [float(m) for m in parts[1:]]
            
            # Calculate magnitudes and their errors
            dic["true_mag"], dic["true_mag_err"] = GullsParser.get_magnitudes(
                df["true_relative_flux"].to_numpy(),
                df["fs"].to_numpy(),
                df["ms"].to_numpy(),
                df["observatory_code"].to_numpy()
            )
            dic["mag"], dic["mag_err"] = GullsParser.get_magnitudes(
                df["measured_relative_flux"].to_numpy(),
                df["fs"].to_numpy(),
                df["ms"].to_numpy(),
                df["observatory_code"].to_numpy()
            )

            # look up the zero points for the flux calculation
            elements = self.filters
            if not len(elements) == len(df["observatory_code"].unique()):
                raise ValueError("Number of elements does not match the number of unique observatory codes.\n"
                                 "You can change the observatory codes using the 'filters' attribute.\n"
                                 "Currently, the filters are: " + ", ".join(self.filters) + " and the unique "
                                 "observatory codes are: " + ", ".join(df["observatory_code"].unique()))
            zp = GullsParser.get_zeropoint(elements)
            
            # Calculate the fluxes
            dic["true_F"], dic["true_F_err"] = GullsParser.get_fluxes(
                dic["true_mag"],
                dic["true_mag_err"],
                df["observatory_code"].to_numpy(),
                zp
            )
            dic["F"], dic["F_err"] = GullsParser.get_fluxes(
                dic["mag"],
                dic["mag_err"],
                df["observatory_code"].to_numpy(),
                zp
            )

            # Add the parameters from the master file to the dictionary
            for gulls_key, df_key in self.master_column_mapping.items():
                if df_key in row.columns:
                    dic[df_key] = row[gulls_key].values[0]
                else:
                    raise KeyError(f"Key '{gulls_key}' not found in master file for {data_file.name}")

            
            if add_astrometry:
                ##################################################################
                # Here you would add your astrometric processing logic
                # For now, we just add 4 dummy columns the same length as BJD and
                # save the DataFrame to the output directory
                dic["data"]["sigma_x"] = 0
                dic["data"]["sigma_y"] = 0
                dic["data"]["sigma_x_err"] = 0
                dic["data"]["sigma_y_err"] = 0
                ##################################################################

                # Add the new columns to the header
                # we are just being explicit to be careful
                header += ["sigma_x", "sigma_y", "sigma_x_err", "sigma_y_err"]
                if header != dic["data"].columns.tolist():
                    raise ValueError("Header does not match DataFrame columns.")

            output_path = self.output_single_lens_dir / data_file.name
            GullsParser.save_lc_output(dic["data"], output_path, header, comment_text)

    def process_binary_lens(self, add_astrometry=True):
        """
        Process binary lens data and save the output.
        """
        # load master file(s) with meta data (.csv, .out)
        self.load_binary_lens_master()

        # load data files (.lc,  .dat)
        data_files = list(self.binary_lens_dir.glob("*.lc")) + list(self.binary_lens_dir.glob("*.dat"))
        if not data_files:
            raise FileNotFoundError(f"No data files found in: {self.binary_lens_dir}")

        # Process each data file
        for data_file in data_files:

            # Strip the file name to get the SubRun, EventID, and Field
            file_name = data_file.stem
            parts = file_name.split("_")
            SubRun = parts[-3]
            Field = parts[-2]
            EventID = parts[-1] 

            # get row from master file based on SubRun, Field, and EventID
            row = self.binary_lens_master[
                (self.binary_lens_master["SubRun"] == SubRun) &
                (self.binary_lens_master["Field"] == Field) &
                (self.binary_lens_master["EventID"] == EventID)
            ]

            if row.empty:
                raise ValueError(f"No matching row found in master file for SubRun: {SubRun}, Field: {Field}, EventID: {EventID}")

            # Load the data file
            df, comment_text, header = GullsParser.load_lc_file(data_file)

            dic = {
                "row": row,
                "data": df,
                "BJD": df["BJD"].to_numpy(),
                "obs": df["observatory_code"].to_numpy()
            }

            # Extract parameters from comment text
            for line in comment_text.splitlines():
                if "Obslensmag" in line:
                    parts = line.split()
                    dic["FL_0"] = float(parts[1])
                    dic["FL_1"] = float(parts[2])
                    dic["FL_2"] = float(parts[3])
                    dic["FL"] = [float(f) for f in parts[1:]]
                elif "fs" in line:
                    parts = line.split()
                    dic["FS_0"] = float(parts[1])
                    dic["FS_1"] = float(parts[2])
                    dic["FS_2"] = float(parts[3])
                    dic["fs"] = [float(f) for f in parts[1:]]
                elif "Obssrcmag" in line:
                    parts = line.split()
                    dic["ms_0"] = float(parts[1])
                    dic["ms_1"] = float(parts[2])
                    dic["ms_2"] = float(parts[3])
                    dic["ms"] = [float(m) for m in parts[1:]]

            # Calculate magnitudes and their errors
            dic["true_mag"], dic["true_mag_err"] = GullsParser.get_magnitudes(
                df["true_relative_flux"].to_numpy(),
                df["fs"].to_numpy(),
                df["ms"].to_numpy(),
                df["observatory_code"].to_numpy()
            )
            dic["mag"], dic["mag_err"] = GullsParser.get_magnitudes(
                df["measured_relative_flux"].to_numpy(),
                df["fs"].to_numpy(),
                df["ms"].to_numpy(),
                df["observatory_code"].to_numpy()
            )

            # look up the zero points for the flux calculation
            elements = self.filters
            if not len(elements) == len(df["observatory_code"].unique()):
                raise ValueError("Number of elements does not match the number of unique observatory codes.\n"
                                 "You can change the observatory codes using the 'filters' attribute.\n"
                                 "Currently, the filters are: " + ", ".join(self.filters) + " and the unique "
                                 "observatory codes are: " + ", ".join(df["observatory_code"].unique()))
            zp = GullsParser.get_zeropoint(elements)

            # Calculate the fluxes
            dic["true_F"], dic["true_F_err"] = GullsParser.get_fluxes(
                dic["true_mag"],
                zp
            )
            dic["F"], dic["F_err"] = GullsParser.get_fluxes(
                dic["mag"],
                zp
            )

            # Add the parameters from the master file to the dictionary
            for gulls_key, df_key in self.master_column_mapping.items():
                if df_key in row.columns:
                    dic[df_key] = row[gulls_key].values[0]
                else:
                    raise KeyError(f"Key '{gulls_key}' not found in master file for {data_file.name}")
            # Add additional columns for binary lens systems
            for gulls_key, df_key in self.additional_master_columns_for_2L.items():
                if df_key in row.columns:
                    dic[df_key] = row[gulls_key].values[0]
                else:
                    raise KeyError(f"Key '{gulls_key}' not found in master file for {data_file.name}")
                
            if add_astrometry:
                ##################################################################
                # Here you would add your astrometric processing logic
                # For now, we just add 4 dummy columns the same length as BJD and
                # save the DataFrame to the output directory
                dic["data"]["sigma_x"] = 0
                dic["data"]["sigma_y"] = 0
                dic["data"]["sigma_x_err"] = 0
                dic["data"]["sigma_y_err"] = 0
                ##################################################################

                # Add the new columns to the header
                # we are just being explicit to be careful
                header += ["sigma_x", "sigma_y", "sigma_x_err", "sigma_y_err"]
                if header != dic["data"].columns.tolist():
                    raise ValueError("Header does not match DataFrame columns.")

            # Save the processed DataFrame to the output directory
            output_path = self.output_binary_lens_dir / data_file.name
            GullsParser.save_lc_output(dic["data"], output_path, header, comment_text)

    def process_triple_lens_astrometry(self, add_astrometry=True):
        """
        Process triple lens data and save the output.
        """
        # load master file(s) with meta data (.csv, .out)
        self.load_triple_lens_master()

        # load data files (.lc,  .dat)
        data_files = list(self.triple_lens_dir.glob("*.lc")) + list(self.triple_lens_dir.glob("*.dat"))
        if not data_files:
            raise FileNotFoundError(f"No data files found in: {self.triple_lens_dir}")

        # Process each data file
        for data_file in data_files:

            # Strip the file name to get the SubRun, EventID, and Field
            file_name = data_file.stem
            parts = file_name.split("_")
            SubRun = parts[-3]
            Field = parts[-2]
            EventID = parts[-1] 

            # get row from master file based on SubRun, Field, and EventID
            row = self.triple_lens_master[
                (self.triple_lens_master["SubRun"] == SubRun) &
                (self.triple_lens_master["Field"] == Field) &
                (self.triple_lens_master["EventID"] == EventID)
            ]

            if row.empty:
                raise ValueError(f"No matching row found in master file for SubRun: {SubRun}, Field: {Field}, EventID: {EventID}")

            # Load the data file
            df, comment_text, header = GullsParser.load_lc_file(data_file)

            dic = {
                "row": row,
                "data": df,
                "BJD": df["BJD"].to_numpy(),
                "obs": df["observatory_code"].to_numpy()
            }

            # Extract parameters from comment text
            for line in comment_text.splitlines():
                if "Obslensmag" in line:
                    parts = line.split()
                    dic["FL_0"] = float(parts[1])
                    dic["FL_1"] = float(parts[2])
                    dic["FL_2"] = float(parts[3])
                    dic["FL"] = [float(f) for f in parts[1:]]
                elif "fs" in line:
                    parts = line.split()
                    dic["FS_0"] = float(parts[1])
                    dic["FS_1"] = float(parts[2])
                    dic["FS_2"] = float(parts[3])
                    dic["fs"] = [float(f) for f in parts[1:]]
                elif "Obssrcmag" in line:
                    parts = line.split()
                    dic["ms_0"] = float(parts[1])
                    dic["ms_1"] = float(parts[2])
                    dic["ms_2"] = float(parts[3])
                    dic["ms"] = [float(m) for m in parts[1:]]

            # Calculate magnitudes and their errors
            dic["true_mag"], dic["true_mag_err"] = GullsParser.get_magnitudes(
                df["true_relative_flux"].to_numpy(),
                df["true_relative_flux_error"].to_numpy()
            )
            dic["mag"], dic["mag_err"] = GullsParser.get_magnitudes(
                df["measured_relative_flux"].to_numpy(),
                df["measured_relative_flux_error"].to_numpy()
            )

            # look up the zero points for the flux calculation
            elements = self.filters
            if not len(elements) == len(df["observatory_code"].unique()):
                raise ValueError("Number of elements does not match the number of unique observatory codes.\n"
                                 "You can change the observatory codes using the 'filters' attribute.\n"
                                 "Currently, the filters are: " + ", ".join(self.filters) + " and the unique "
                                 "observatory codes are: " + ", ".join(df["observatory_code"].unique()))
            zp = GullsParser.get_zeropoint(elements)

            # Calculate the fluxes
            dic["true_F"], dic["true_F_err"] = GullsParser.get_fluxes(
                dic["true_mag"],
                dic["true_mag_err"],
                df["observatory_code"].to_numpy(),
                zp
            )
            dic["F"], dic["F_err"] = GullsParser.get_fluxes(
                dic["mag"],
                dic["mag_err"],
                df["observatory_code"].to_numpy(),
                zp
            )

            # Add the parameters from the master file to the dictionary
            for gulls_key, df_key in self.master_column_mapping.items():
                if df_key in row.columns:
                    dic[df_key] = row[gulls_key].values[0]
                else:
                    raise KeyError(f"Key '{gulls_key}' not found in master file for {data_file.name}")
            # Add additional columns for binary lens systems
            for gulls_key, df_key in self.additional_master_columns_for_2L.items():
                if df_key in row.columns:
                    dic[df_key] = row[gulls_key].values[0]
                else:
                    raise KeyError(f"Key '{gulls_key}' not found in master file for {data_file.name}")
            # Add additional columns for triple lens systems
            for gulls_key, df_key in self.additional_master_columns_for_3L.items():
                if df_key in row.columns:
                    dic[df_key] = row[gulls_key].values[0]
                else:
                    raise KeyError(f"Key '{gulls_key}' not found in master file for {data_file.name}")
            
            if add_astrometry:
                ##################################################################
                # Here you would add your astrometric processing logic
                # For now, we just add 4 dummy columns the same length as BJD and
                # save the DataFrame to the output directory
                dic["data"]["sigma_x"] = 0
                dic["data"]["sigma_y"] = 0
                dic["data"]["sigma_x_err"] = 0
                dic["data"]["sigma_y_err"] = 0
                ##################################################################

                # Add the new columns to the header
                # we are just being explicit to be careful
                header += ["sigma_x", "sigma_y", "sigma_x_err", "sigma_y_err"]
                if header != dic["data"].columns.tolist():
                    raise ValueError("Header does not match DataFrame columns.")
            
            # Save the processed DataFrame to the output directory
            output_path = self.output_triple_lens_dir / data_file.name
            GullsParser.save_lc_output(dic["data"], output_path, header, comment_text)

    def process_all_astrometry(self, single=False, binary=False, triple=False, add_astrometry=True):
        """
        Process all lens types: single, binary, and triple.
        """
        if single:
            self.process_single_lens(add_astrometry=add_astrometry)
        if binary:
            self.process_binary_lens(add_astrometry=add_astrometry)
        if triple:
            self.process_triple_lens(add_astrometry=add_astrometry)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Process GULLS light curve data.")
    parser.add_argument("--input_dir", type=str, default="input", help="Input directory containing GULLS data.")
    parser.add_argument("--output_dir", type=str, default="output", help="Output directory for processed data.")
    parser.add_argument("--single", action="store_true", help="Process single lens systems.")
    parser.add_argument("--binary", action="store_true", help="Process binary lens systems.")
    parser.add_argument("--triple", action="store_true", help="Process triple lens systems.")
    parser.add_argument("--add_astrometry", action="store_true", help="Add simulatedastrometric data.")

    args = parser.parse_args()

    # Create the parser instance
    parser = GullsParser(input_dir=args.input_dir, output_dir=args.output_dir)

    # Process all, if none are specified
    if not args.single and not args.binary and not args.triple: 
        args.single = True
        args.binary = True
        args.triple = True
    
    # Process all lens types
    parser.process_all_astrometry(
        single=args.single, 
        binary=args.binary, 
        triple=args.triple, 
        add_astrometry=args.add_astrometry
    )