

def arg_list(parser):
    parser.add_argument('--grep', type=str, action='append',
                        help='Regexp to grep the clouds by names')

    return parser


def arg_show(parser):
    parser.add_argument('cloud', nargs='?', type=str, action='store', default=None,
                        help='Cloud name to show')

    return parser
