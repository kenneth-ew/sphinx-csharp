class ExternalRefsData:
    """ This class just holds data used for external linking. Keeps data separate from functionality """

    shorten_type_prefixes = [
        'System.',
        'System.IO',
        'System.Collections.Generic.',
    ]

    """ Types and strings to ignore when looking for a reference """
    ignore_xref_types = [
        '*',
        '&',
        'void',

        # Built-in value types 
        # https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types
        'bool',
        'byte',
        'sbyte',
        'char',
        'decimal',
        'double',
        'float',
        'int',
        'uint',
        'nint',
        'nuint',
        'long',
        'ulong',
        'short',
        'ushort',
        
        # Built-in reference types
        'object',
        'string',
        'dynamic',
    ]

    """
    Contains recognised types and their namespaces as well as the package name.
    The package name references the key in external_search_pages

    Format the content like this:
    Where Namespace1 is the namespace for the link (which may not match the real namespace)::

        'package': {
            'Namespace1': ['member1', ...],
            ...
        },
        ...
    """
    external_type_map = {
        'msdn': {
            'System': ['Tuple', 'IDisposable', 'ICloneable', 'IComparable', 'Func', 'Action',
                       'Int16', 'Int32', 'Int64', 'Int128', 'UInt16', 'UInt32', 'UInt64', 'UInt128'],
            'System.Collections': ['IEnumerator'],
            'System.Collections.Generic': ['List', 'Dictionary', 'IList', 'IDictionary', 'ISet', 'IEnumerable'],
            'System.IO': ['FileFormatException'],
            'System.Threading': ['Thread'],
            'System.Runtime.InteropServices': ['GCHandle', 'Marshal'],
        },
        'unity': {
            '': ['MonoBehaviour', 'ScriptableObject',
                 'GameObject', 'Transform', 'RectTransform',
                 'Mesh', 'MeshRenderer', 'MeshFilter', 'Animator',
                 'Collider', 'SphereCollider', 'BoxCollider',
                 'Material', 'Sprite',
                 'Vector2', 'Vector3', 'Vector4', 'Quaternion', 'Color', 'Gradient',
                 'Coroutine', 'Space', 'LayerMask', 'Layer',
                 'AssetPostprocessor',
                 ],
        },
    }

    """
    Put special cases in here that should be renamed when used in links, use it for generics
    The name is swapped *after* searching EXTERNAL_TYPE_MAP, just before constructing the url link
    """
    external_type_rename = {
        'List': 'List-1',
        'Dictionary': 'Dictionary-2',
        'IList': 'IList-1',
        'IDictionary': 'IDictionary-2',
        'ISet': 'ISet-2',
        'IEnumerable': 'IEnumerable-1',
        'Func': 'Func-1',
    }

    """
    Where do we search for api documentation
    Syntax:
    'package': ('api link', 'fallback search link')
    Use %s for where to substitute item, every link *must* contain this
    """
    external_search_pages = {
        'msdn': ('https://docs.microsoft.com/en-us/dotnet/api/%s',
                 'https://docs.microsoft.com/en-us/search/?category=All&scope=.NET&terms=%s'),
        'unity': ('https://docs.unity3d.com/ScriptReference/%s.html',
                  'https://docs.unity3d.com/ScriptReference/30_search.html?q=%s'),
        'unityman': ('https://docs.unity3d.com/Manual/%s.html',
                     'https://docs.unity3d.com/Manual/30_search.html?q=%s'),
    }
