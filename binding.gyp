{
	"targets": [
		{
			"target_name": "injector",
			"cflags!": [
				"-fno-exceptions"
			],
			"cflags_cc!": [
				"-fno-exceptions"
			],
			"sources": [
				"injector.cpp"
			],
			"include_dirs": [
				"<!@(node -p \"require('node-addon-api').include\")"
			],
			"libraries": [],
			"dependencies": [
				"<!(node -p \"require('node-addon-api').gyp\")"
			],
			"defines": [ 
            	"NAPI_DISABLE_CPP_EXCEPTIONS",
				"NAPI_VERSION=<(napi_build_version)",
			]
		}
	]
}