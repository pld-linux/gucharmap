Summary:	Unicode character map
Summary(pl):	Mapa znaków Unikodowych
Name:		gucharmap
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.4/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	pango-devel >= 1.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gucharmap is a featureful unicode character map.

%description -l pl
Gucharmap jest warto¶ciow± map± znaków Unikodowych.

%package devel
Summary:	Headers for gucharmap
Summary(pl):	Pliki nag³ówkowe gucharmap
Group:		Development/Libraries
Requires:	%{name} = %{version}
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	pango-devel >= 1.2.1

%description devel
The gucharmap-devel package includes the libraries and include files
that you will need to use gucharmap.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i biblioteki potrzebne do
kompilacji programów u¿ywaj±cych gucharmap.

%package static
Summary:  Static gucharmap libraries
Summary(pl):  Statyczne biblioteki gucharmap
Group:    X11/Development/Libraries
Requires: %{name}-devel = %{version}
%description static
Static version of gucharmap libraries.

%description static -l pl
Statyczna wersja bibliotek gucharmap.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf gucharmap $RPM_BUILD_ROOT%{_bindir}/charmap

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*charmap
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_datadir}/applications/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/*.la
%{_pkgconfigdir}/*

%files static
%{_libdir}/*.a
