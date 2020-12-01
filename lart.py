{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}




{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}


{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}


{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}


{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}




{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}


{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}


{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}


{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}




{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}


{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}


{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}


{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}




{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}


{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}


{
 "metadata": {
  "name": "",
  "signature": "sha256:d3e9ccec3aa008902fdce1dfd54a45c32dd4d341a129f2d73bdf2a7e33810e13"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr = {'shape':'circle','size':'very large','fill':'no','inside':'b'}\n",
      "b_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 13
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_attr = {'shape':'square','size':'medium','fill':'no','inside':'d'}\n",
      "d_attr = {'shape':'circle','size':'huge','fill':'no'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "e_attr = {'shape':'circle','size':'very large','fill':'no','inside':'f'}\n",
      "f_attr = {'shape':'circle','size':'huge','fill':'no'}\n",
      "s_attr = {'shape':'square','size':'very small','fill':'yes','inside':['f','e']}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 15
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.keys()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "['shape', 'fill', 'inside', 'size']"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_attr.values()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 10,
       "text": [
        "['circle', 'no', 'b', 'very large']"
       ]
      }
     ],
     "prompt_number": 10
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a_attr.items()\n",
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 21,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('inside', 'b'), ('size', 'very large')]"
       ]
      }
     ],
     "prompt_number": 21
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_attr.items()\n",
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 19,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 19
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples = a_tuples + b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 22
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 23,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 23
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "c_tuples = c_attr.items()\n",
      "c_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 24,
       "text": [
        "[('shape', 'square'), ('fill', 'no'), ('inside', 'd'), ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 24
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "d_tuples = d_attr.items()\n",
      "d_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 26,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 26
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples = c_tuples + d_tuples\n",
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 27,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 27
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples - cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "ename": "TypeError",
       "evalue": "unsupported operand type(s) for -: 'list' and 'list'",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
        "\u001b[0;32m<ipython-input-28-1c98da6467b3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mab_tuples\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0mcd_tuples\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
        "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'list' and 'list'"
       ]
      }
     ],
     "prompt_number": 28
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "set(ab_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 29,
       "text": [
        "{('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('shape', 'circle'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'very large')}"
       ]
      }
     ],
     "prompt_number": 29
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only = dict(list(set(ab_tuples) - set(cd_tuples)))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 30
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 31,
       "text": [
        "{'inside': 'b', 'size': 'very large'}"
       ]
      }
     ],
     "prompt_number": 31
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_att_only = dict(list(set(cd_tuples) - set(ab_tuples)))\n",
      "cd_att_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 32,
       "text": [
        "{'inside': 'd', 'shape': 'square', 'size': 'medium'}"
       ]
      }
     ],
     "prompt_number": 32
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 33,
       "text": [
        "[('shape', 'square'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'd'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 33
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 34,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'b'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 34
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "ab_tuples_only = list(set(ab_tuples) - set(cd_tuples))\n",
      "ab_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 43,
       "text": [
        "[('size', 'very large'), ('inside', 'b')]"
       ]
      }
     ],
     "prompt_number": 43
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "cd_tuples_only = list(set(cd_tuples) - set(ab_tuples))\n",
      "cd_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 44,
       "text": [
        "[('size', 'medium'), ('inside', 'd'), ('shape', 'square')]"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A = [('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 47
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B =[('shape','circle'),('size', 'very large'),('fill','no'),('shape','plus'),('size','small'),('fill','yes'),('angel',0),('inside','a')]\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 48
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only = list(set(A) - set(B))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 49
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 50,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 50
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a={'shape':'right triangle', 'fill':'yes','angle':270,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 60
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples = a.items()\n",
      "print a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]\n"
       ]
      }
     ],
     "prompt_number": 179
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 62,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 270),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 62
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = {'shape':'right triangle', 'fill':'yes','angle':0,'size':'very large'}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 63
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples = b_tuples.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 64
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 65,
       "text": [
        "[('shape', 'right triangle'),\n",
        " ('size', 'very large'),\n",
        " ('angle', 0),\n",
        " ('fill', 'yes')]"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only = list(set(a_tuples) - set(b_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 66
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 68,
       "text": [
        "[('angle', 270)]"
       ]
      }
     ],
     "prompt_number": 68
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only = list(set(b_tuples) - set(a_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 72
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "b_tuples_only"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 73,
       "text": [
        "[('angle', 0)]"
       ]
      }
     ],
     "prompt_number": 73
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = {'shape':'circle','size':'huge','fill':'no'}\n",
      "b = {'shape':'circle','size':'very large','fill':'no','inside':'a'}\n",
      "c = {'shape':'circle','size':'large','fill':'no','inside':('a','b')}\n",
      "d = {'shape':'circle','size':'medium','fill':'no','inside':('a','b','c')}\n",
      "e = {'shape':'circle','size':'small','fill':'no','inside':('a','b','c','d')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 144
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = a.items()+b.items()+c.items()+d.items()+e.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 145
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 146,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 146
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "f = {'shape':'circle','size':'large','fill':'no'}\n",
      "g = {'shape':'circle','size':'medium','fill':'no','inside':'f'}\n",
      "h = {'shape':'circle','size':'small','fill':'no','inside':('f','g')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 147
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples = f.items()+g.items()+h.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 148
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 149,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 149
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "i = {'shape':'circle','size':'huge','fill':'no'}\n",
      "j = {'shape':'circle','size':'very large','fill':'no','inside':'i'}\n",
      "k = {'shape':'circle','size':'large','fill':'no','inside':('j','i')}"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 150
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples = i.items()+j.items()+k.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 151
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 152,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'i'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('j', 'i')),\n",
        " ('size', 'large')]"
       ]
      }
     ],
     "prompt_number": 152
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 153,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'f'),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('f', 'g')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 153
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 154
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 155,
       "text": [
        "[('size', 'very large'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 155
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "list(set(A_not_in_B_tuples) & set(a.items()))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 178,
       "text": [
        "[('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 178
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples = list(set(B_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 156
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "B_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 157,
       "text": [
        "[('inside', 'f'), ('inside', ('f', 'g'))]"
       ]
      }
     ],
     "prompt_number": 157
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples = list(set(A_tuples) - set(C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 158
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_in_C_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 159,
       "text": [
        "[('inside', ('a', 'b', 'c')),\n",
        " ('size', 'small'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('inside', ('a', 'b')),\n",
        " ('inside', 'a'),\n",
        " ('size', 'medium')]"
       ]
      }
     ],
     "prompt_number": 159
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 169,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'huge'}"
       ]
      }
     ],
     "prompt_number": 169
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples = list(set(C_tuples) - set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 160
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_not_in_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 161,
       "text": [
        "[('inside', ('j', 'i')), ('inside', 'i')]"
       ]
      }
     ],
     "prompt_number": 161
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples = list(set(C_tuples) & set(A_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 162
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "C_and_A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 163,
       "text": [
        "[('size', 'very large'),\n",
        " ('size', 'huge'),\n",
        " ('size', 'large'),\n",
        " ('fill', 'no'),\n",
        " ('shape', 'circle')]"
       ]
      }
     ],
     "prompt_number": 163
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "dict(C_and_A_tuples)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 131,
       "text": [
        "{'fill': 'no', 'shape': 'circle', 'size': 'large'}"
       ]
      }
     ],
     "prompt_number": 131
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a.items()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 134,
       "text": [
        "[('shape', 'circle'), ('fill', 'no'), ('size', 'huge')]"
       ]
      }
     ],
     "prompt_number": 134
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score = list(set(a.items()) & set(A_not_in_C_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 167
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a_score"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 168,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 168
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 170,
       "text": [
        "[('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('size', 'huge'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', 'a'),\n",
        " ('size', 'very large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b')),\n",
        " ('size', 'large'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c')),\n",
        " ('size', 'medium'),\n",
        " ('shape', 'circle'),\n",
        " ('fill', 'no'),\n",
        " ('inside', ('a', 'b', 'c', 'd')),\n",
        " ('size', 'small')]"
       ]
      }
     ],
     "prompt_number": 170
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_tuples = [('shape', 'circle')]\n",
      "B_tuples = [('shape', 'circle')]"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 183
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples = list(set(A_tuples) - set(B_tuples))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 184
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "A_not_B_tuples"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 185,
       "text": [
        "[]"
       ]
      }
     ],
     "prompt_number": 185
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}

