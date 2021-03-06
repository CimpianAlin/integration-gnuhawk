#!/usr/bin/env python
#
# Copyright 2009,2010 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest

class test_copy_octet(gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_copy (self):
        src_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        expected_result = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        src = gr.vector_source_b(src_data)
        op = gr.copy(gr.sizeof_char, True,1)
        dst = gr.vector_sink_b()
        self.tb.connect(src, op, dst)
        self.tb.run()
        dst_data = dst.data()
        self.assertEqual(expected_result, dst_data)

    def test_copy_drop (self):
        src_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        expected_result = ()
        src = gr.vector_source_b(src_data)
        op = gr.copy(gr.sizeof_char, False, 1)
        #op.enable = True
        dst = gr.vector_sink_b()
        self.tb.connect(src, op, dst)
        self.tb.run()
        dst_data = dst.data()
        self.assertEqual(expected_result, dst_data)

class test_copy_complex(gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_copy (self):
        src_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        expected_result = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        src = gr.vector_source_c(src_data)
        op = gr.copy(gr.sizeof_gr_complex, True,8)
        dst = gr.vector_sink_c()
        self.tb.connect(src, op, dst)
        self.tb.run()
        dst_data = dst.data()
        self.assertEqual(expected_result, dst_data)

    def test_copy_drop (self):
        src_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        expected_result = ()
        src = gr.vector_source_c(src_data)
        op = gr.copy(gr.sizeof_gr_complex, False, 8)
        dst = gr.vector_sink_c()
        self.tb.connect(src, op, dst)
        self.tb.run()
        dst_data = dst.data()
        self.assertEqual(expected_result, dst_data)

class test_copy_int(gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_copy (self):
        src_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        expected_result = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        src = gr.vector_source_i(src_data)
        op = gr.copy(gr.sizeof_int, True,4)
        dst = gr.vector_sink_i()
        self.tb.connect(src, op, dst)
        self.tb.run()
        dst_data = dst.data()
        self.assertEqual(expected_result, dst_data)

    def test_copy_drop (self):
        src_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        expected_result = ()
        src = gr.vector_source_i(src_data)
        op = gr.copy(gr.sizeof_int, False, 4)
        dst = gr.vector_sink_i()
        self.tb.connect(src, op, dst)
        self.tb.run()
        dst_data = dst.data()
        self.assertEqual(expected_result, dst_data)

class test_copy_short(gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_copy (self):
        src_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        expected_result = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        src = gr.vector_source_s(src_data)
        op = gr.copy(gr.sizeof_short, True,2)
        dst = gr.vector_sink_s()
        self.tb.connect(src, op, dst)
        self.tb.run()
        dst_data = dst.data()
        self.assertEqual(expected_result, dst_data)

    def test_copy_drop (self):
        src_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        expected_result = ()
        src = gr.vector_source_s(src_data)
        op = gr.copy(gr.sizeof_short, False, 2)
        dst = gr.vector_sink_s()
        self.tb.connect(src, op, dst)
        self.tb.run()
        dst_data = dst.data()
        self.assertEqual(expected_result, dst_data)


if __name__ == '__main__':
    gr_unittest.run(test_copy, "test_copy.xml")
