# coding: utf8

# Change directories you want to ignore here
ignore_directories = {
    'common': [
        'vendor',
        'build',
    ],
    'Go': [
        'thrift_gen',
        'clients',  # This dir is not universal for Go, delete it if you don't want to ignore
    ],
    'Python': [
        'develop-eggs',
        'dist',
        'eggs',
        'lib',
        'lib64',
        'wheels',
        'env',
    ],
    'C++': [

    ],
    'Java': [

    ],
    'C': [

    ],
    'JavaScript': [

    ],
    'C#': [

    ],
    'Ruby': [

    ],
}

# If linguist doesn't work, then code file's language are detected according to this config.
code_file_extensions = {
    'py': 'Python',
    'go': 'Go',
    'c': 'C',
    'h': 'C++',
    'cpp': 'C++',
    'cc': 'C++',
    'hpp': 'C++',
    'java': 'Java',
    'js': 'JavaScript',
    'vue': 'JavaScript',
    'ts': 'TypeScript',
    'css': 'CSS',
    'less': 'CSS',
    'html': 'HTML',
    'cs': 'C#',
    'php': 'PHP',
    'r': 'R',
    'rb': 'Ruby',
    'm': 'Objective-C',
    'swift': 'Swift',
    'scala': 'Scala',
    'sh': 'Shell',
}
