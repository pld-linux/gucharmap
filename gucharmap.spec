#
# Conditional build:
%bcond_without	static_libs		# static library
%bcond_without	vala			# Vala API
%bcond_with	system_unicode_ucd	# use data from unicode-ucd package instead of separate sources

%define		unicode_ver	16.0.0

Summary:	Unicode character map
Summary(pl.UTF-8):	Mapa znaków unikodowych
Name:		gucharmap
Version:	16.0.2
Release:	1
License:	GPL v3+
Group:		X11/Applications
#Source0Download: https://gitlab.gnome.org/GNOME/gucharmap/-/tags
Source0:	https://gitlab.gnome.org/GNOME/gucharmap/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	b349d3a7d5606a934a1a5fe71a7550f0
%if %{without system_unicode_ucd}
Source1:	http://www.unicode.org/Public/%{unicode_ver}/ucd/Blocks.txt
# Source1-md5:	f9f7b6476b2649553fa8cdc5544f804a
Source2:	http://www.unicode.org/Public/%{unicode_ver}/ucd/DerivedAge.txt
# Source2-md5:	b848bf714511f1212cea3519a89b29d3
Source3:	http://www.unicode.org/Public/%{unicode_ver}/ucd/NamesList.txt
# Source3-md5:	6c53d0a345f50ce94b9706d86cb44724
Source4:	http://www.unicode.org/Public/%{unicode_ver}/ucd/Scripts.txt
# Source4-md5:	64db902717355c3fc8eee3d125de92cf
Source5:	http://www.unicode.org/Public/%{unicode_ver}/ucd/UnicodeData.txt
# Source5-md5:	f50a0495d2000b7d6dd979cb40e00ba2
Source6:	http://www.unicode.org/Public/%{unicode_ver}/ucd/Unihan.zip
# Source6-md5:	aa81fdcb61759c4b8316f2c43d24fc5e
%endif
URL:		https://wiki.gnome.org/Apps/Gucharmap
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-dtd412-xml
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libxml2-progs
BuildRequires:	meson >= 0.62.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pcre2-8-devel >= 10.21
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
%if %{with system_unicode_ucd}
BuildRequires:	unicode-ucd = %{unicode_ver}
BuildRequires:	unicode-ucd-unihan = %{unicode_ver}
%endif
%{?with_vala:BuildRequires:	vala >= 2:0.24.0-2}
BuildRequires:	unzip
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,preun):	glib2 >= 1:2.32.0
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gucharmap is a featureful unicode character map.

%description -l pl.UTF-8
Gucharmap jest wartościową mapą znaków unikodowych.

%package libs
Summary:	gucharmap library for GTK+ 3
Summary(pl.UTF-8):	Biblioteka gucharmap dla GTK+ 3
Group:		X11/Libraries
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.4.0
Requires:	pango >= 1:1.20.0
Requires:	pcre2-8 >= 10.21

%description libs
This package contains gucharmap library for GTK+ 3.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę gucharmap dla GTK+ 3.

%package devel
Summary:	Headers for gucharmap (GTK+ 3 verson)
Summary(pl.UTF-8):	Pliki nagłówkowe gucharmap (wersja dla GTK+ 3)
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.32.0
Requires:	gtk+3-devel >= 3.4.0
Requires:	pcre2-8-devel >= 10.21

%description devel
The gucharmap-devel package includes the header files that you will
need to use gucharmap. This version is targeted for GTK+ 3.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
używających gucharmap. Ta wersja jest przeznaczona dla GTK+ 3.

%package static
Summary:	Static gucharmap library for GTK+ 3
Summary(pl.UTF-8):	Statyczna biblioteka gucharmap dla GTK+ 3
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of gucharmap library for GTK+ 3.

%description static -l pl.UTF-8
Statyczna wersja biblioteki gucharmap dla GTK+ 3.

%package apidocs
Summary:	gucharmap library API documentation (GTK+ 3 version)
Summary(pl.UTF-8):	Dokumentacja API biblioteki gucharmap (wersja dla GTK+ 3)
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
gucharmap library API documentation (GTK+ 3 version).

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gucharmap (wersja dla GTK+ 3).

%package -n vala-gucharmap
Summary:	gucharmap API for Vala language
Summary(pl.UTF-8):	API gucharmap dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.24.0-2
BuildArch:	noarch

%description -n vala-gucharmap
gucharmap API for Vala language.

%description -n vala-gucharmap -l pl.UTF-8
API gucharmap dla języka Vala.

%prep
%setup -q

%if %{without system_unicode_ucd}
install -d unicode-data
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} unicode-data
%endif

%if %{with static_libs}
%{__sed} -i -e '/^libgucharmap_gtk3 = / s/shared_library/library/' gucharmap/meson.build
%endif

%build
%meson \
	-Ducd_path=%{?with_system_unicode_ucd:%{_datadir}/unicode/ucd}%{!?with_system_unicode_ucd:$(pwd)/unicode-data} \
	%{!?with_vala:-Dvapi=false}

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING.UNICODE README.md TODO
%attr(755,root,root) %{_bindir}/gucharmap
%{_desktopdir}/gucharmap.desktop
%{_datadir}/metainfo/gucharmap.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Charmap.gschema.xml

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgucharmap_2_90.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgucharmap_2_90.so.7
%{_libdir}/girepository-1.0/Gucharmap-2.90.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgucharmap_2_90.so
%{_includedir}/gucharmap-2.90
%{_pkgconfigdir}/gucharmap-2.90.pc
%{_datadir}/gir-1.0/Gucharmap-2.90.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgucharmap_2_90.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gucharmap-2.90

%if %{with vala}
%files -n vala-gucharmap
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gucharmap-2.90.deps
%{_datadir}/vala/vapi/gucharmap-2.90.vapi
%endif
