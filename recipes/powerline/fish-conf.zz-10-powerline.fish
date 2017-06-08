
if status --is-interactive

	add_to_path ~/Library/Python/2.7/bin/
	add_to_path ~/.local/bin/

	powerline-daemon --quiet

	set -q POWERLINE_SITE_PACKAGE; or set --universal POWERLINE_SITE_PACKAGE (string trim -l (pip show powerline-status | grep Location | cut -f 2 -d :))

	set fish_function_path $fish_function_path $POWERLINE_SITE_PACKAGE/powerline/bindings/fish

	powerline-setup

end
