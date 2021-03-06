import subprocess
import pytest

from ..helpers import BaseACS


class TestSingle(BaseACS):
    """
    Process single HRC dataset using using all standard calibration 
    steps.

    Process single HRC dataset with DQICORR, BLEVCORR, BIASCORR,
    DARKCORR, FLATCORR, PHOTCORR, RPTCORR, and DITHCORR set to PERFORM.
    RPTCORR not actually done as there is only one image.

    Process single HRC dataset using using all standard calibration 
    steps and FLSHCORR.
    """
    detector = 'hrc'

    def _single_raw_calib(self, rootname):
        raw_file = '{}_raw.fits'.format(rootname)

        # Prepare input file.
        self.get_input_file(raw_file)

        # Run CALACS
        subprocess.call(['calacs.e', raw_file, '-v'])

        # Compare results
        outputs = [('{}_flt.fits'.format(rootname),
                    '{}_flt_ref.fits'.format(rootname))]
        self.compare_outputs(outputs)

    # NOTE:
    # j8bt02loq = was hrc_single1
    # j8cd02tyq = was hrc_single2
    # j8bt02lo2 = was hrc_single3 with FLSHCORR
    @pytest.mark.parametrize(
        'rootname', ['j8bt02loq', 'j8cd02tyq', 'j8bt02lo2'])
    def test_fullframe_single(self, rootname):
        self._single_raw_calib(rootname)

