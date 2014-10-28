# This file is part of sequence-aligner.
# Copyright (C) 2014 Christopher Kyle Horton <chorton@ltu.edu>

# sequence-aligner is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# sequence-aligner is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with sequence-aligner. If not, see <http://www.gnu.org/licenses/>.


# MCS 5603 Intro to Bioinformatics, Fall 2014
# Christopher Kyle Horton (000516274), chorton@ltu.edu
# Last modified: 10/28/2014

class scoring_matrix:
    '''A class implementing a scoring matrix.'''
    def __init__(self, sequence_length1, sequence_length2):
        '''Initializes a new scoring matrix with the supplied sequence
        lengths.'''
        seql = (sequence_length1 + 1, sequnece_length2 + 1)
        self.matrix = [[0 for x in range(seql[0])] for x in range(seql[1])]
