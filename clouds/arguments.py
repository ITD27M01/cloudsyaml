def arg_show(parser):
    parser.add_argument('cloud', nargs='?', type=str, action='store', default=None,
                        help='Cloud name to show')

    return parser
