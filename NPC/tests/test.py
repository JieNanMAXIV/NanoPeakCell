options_EIGER = {'detector': 'Eiger4M',
                 'experiment': 'SSX',
                 'detector_distance': 100,
                 'beam_x': 502,
                 'beam_y': 515,
                 'wavelength': 0.832,
                 'output_directory': '.',
                 'num': 1,
                 'output_formats': '',
                 'data': '/Users/nico/Eiger/temp_data',
                 'root': '',
                 'file_extension': '.h5',
                 'randomizer': False,
                 'cpus': 4,
                 'threshold': 10,
                 'npixels': 30,
                 'background_subtraction': 'None',
                 'bragg_search': False

               }
options_SACLA = {
               'experiment' : 'SFX_SACLA',
               'detector_distance' : 100,
               'beam_x' : 502,
               'beam_y' : 515,
               'wavelength' : 0.832,
               'output_directory' : '.',
               'num' : 1,
               'output_formats': '',
               'data' : '/Users/nico/IBS2013/SERIALX/IRISFP',
               'root': 'shot',
               'file_extension': '.h5',
               'randomizer': False,
               'runs': '1-2',
               'cpus': 4,
               'threshold': 1000,
               'npixels': 100,
               'background_subtraction': 'None',
               'bragg_search': False
               }

options_SSX = { 'detector' : 'Pilatus6M',
               'experiment' : 'SSX',
               'detector_distance' : 100,
               'beam_x' : 502,
               'beam_y' : 515,
               'wavelength' : 0.832,
               'output_directory' : '.',
               'num' : 1,
               'output_formats': '',
               'data' : '/Users/nico/IBS2013/Ubi/img',
               'root': 'b3rod',
               'file_extension': '.cbf',
               'randomizer': 100,
               'cpus': 4,
               'threshold': 100,
               'npixels': 100,
               'background_subtraction': 'None',
               'bragg_search': False,
               'bragg_threshold': 10
               }