{
	"targets": [
		{
			"target_name": "injector",
			"sources": [
				"injector.cc",
				"functions.cc"
			],
			"include_dirs": [
				"<!(node -e \"require('nan')\")"
			],
			"msvs_settings": {
				"VCCLCompilerTool": {
					"AdditionalOptions": [
						"-std:c++17"
					]
				}
			},
			"defines": [
              "NAPI_VERSION=<(napi_build_version)"
            ]
		}
	],
    "variables": {
        "openssl_fips": ""
    }
}