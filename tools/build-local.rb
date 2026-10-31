# Local static build using Jekyll's own rendering engine. This avoids loading
# optional live-reload server extensions on a portable Windows Ruby installation.
# The normal supported build is `bundle exec jekyll build` (see README).
ENV['JEKYLL_NO_BUNDLER_REQUIRE'] = 'true'
root = File.expand_path('..', __dir__)
gem_root = File.join(root, 'working/gems/ruby/3.3.0')
ENV['GEM_HOME'] = gem_root
ENV['GEM_PATH'] = [gem_root, ENV['GEM_PATH']].compact.join(File::PATH_SEPARATOR)
require 'json'
require 'bigdecimal'
$LOAD_PATH.unshift(File.join(gem_root, 'gems/concurrent-ruby-1.3.8/lib/concurrent-ruby'))
Dir[File.join(gem_root, 'gems/*/lib')].reject { |path| path.match?(%r{/(json-|bigdecimal-|eventmachine-|http_parser)}) }.each { |path| $LOAD_PATH.unshift(path) }
require 'jekyll'
config = Jekyll.configuration('source' => root, 'destination' => File.join(root, '_site'), 'baseurl' => ARGV.fetch(0, '/myWebPage'), 'disable_disk_cache' => true)
Jekyll::Site.new(config).process
puts 'Jekyll static build complete.'
